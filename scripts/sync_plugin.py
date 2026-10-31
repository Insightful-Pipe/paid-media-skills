#!/usr/bin/env python3
"""Build this Claude plugin from the skills published on insightfulpipe.com.

The plugin is one slice of the InsightfulPipe skills library. plugins.json in
Insightful-Pipe/marketing-skills says which skills belong to which plugin; this script
reads it, copies this plugin's skills into skills/<slug>/ with exactly the files the site
serves, and regenerates README.md, .claude-plugin/plugin.json and
.claude-plugin/marketplace.json. When anything changes, the plugin version moves on, so
Claude Code and the plugin directory see an update.

Usage: python3 scripts/sync_plugin.py [plugin-name]   (run from the repository root; no dependencies)
The plugin name defaults to the one in .claude-plugin/plugin.json. Set PLUGINS_JSON to a
local file to use a mapping that isn't pushed yet.

Reviewed skills reach GitHub before their site page goes live. The library repo lists them in
queued.json with each file's hash; this plugin takes its share of them from there, checks every
file against its hash, and lists them without a Page link until the site has them.
"""
import base64
import datetime
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.request

SITE = "https://insightfulpipe.com"
PAGES = f"{SITE}/marketing-claude-skills"
MAPPING_URL = "https://raw.githubusercontent.com/Insightful-Pipe/marketing-skills/main/plugins.json"
LIBRARY_RAW = "https://raw.githubusercontent.com/Insightful-Pipe/marketing-skills/main"
LIBRARY = "https://github.com/Insightful-Pipe/marketing-skills"
ORG = "Insightful-Pipe"
# The site refuses the default Python user agent.
USER_AGENT = "InsightfulPipe-plugin-sync/1.0 (+https://github.com/Insightful-Pipe)"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
README = os.path.join(ROOT, "README.md")
PLUGIN = os.path.join(ROOT, ".claude-plugin", "plugin.json")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
LICENSE = os.path.join(ROOT, "LICENSE")
# A catalogue that suddenly drops most of this plugin's skills is far more likely to be a
# site problem than a mass unpublish, so stop rather than delete them.
MAX_REMOVED = 0.5

MIT = """MIT License

Copyright (c) 2026 InsightfulPipe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def fetch(url, accept="application/json"):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except Exception as exc:  # network blips and deploys in progress
            if attempt == 3:
                raise RuntimeError(f"{url}: {exc}") from exc
            time.sleep(5 * (attempt + 1))


def fetch_bytes(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # network blips
            if attempt == 3:
                raise RuntimeError(f"{url}: {exc}") from exc
            time.sleep(5 * (attempt + 1))


def load_queued(live_slugs):
    """Reviewed skills that are in the library repo but not live on the site yet."""
    try:
        entries = fetch(f"{LIBRARY_RAW}/queued.json").get("skills") or []
    except RuntimeError:
        return []
    return [dict(q, queued=True) for q in entries if q["slug"] not in live_slugs and q.get("files")]


def sync_queued_files(skill):
    """Copy a queued skill from the library repo. Returns False (and keeps what is here) if a file doesn't match its hash yet."""
    got = {}
    for f in skill["files"]:
        raw = fetch_bytes(f"{LIBRARY_RAW}/skills/{skill['slug']}/{f['path']}")
        if hashlib.sha256(raw).hexdigest() != f["sha256"]:
            print(f"{skill['slug']}/{f['path']}: the library repo hasn't caught up yet; keeping this skill as it is.")
            return False
        got[f["path"]] = raw
    folder = os.path.join(SKILLS_DIR, skill["slug"])
    os.makedirs(folder, exist_ok=True)
    for rel, raw in got.items():
        target = safe_path(folder, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        if not os.path.exists(target) or open(target, "rb").read() != raw:
            with open(target, "wb") as out:
                out.write(raw)
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            p = os.path.join(dirpath, name)
            if os.path.relpath(p, folder) not in got:
                os.remove(p)
    return True


def load_mapping():
    local = os.environ.get("PLUGINS_JSON")
    return json.load(open(local)) if local else fetch(MAPPING_URL)


def owners(mapping, skills):
    """Map each skill slug to the one plugin that claims it, or stop on a double claim."""
    plugins = mapping["plugins"]
    included = {}
    for p in plugins:
        for slug in p.get("include", []):
            if slug in included:
                sys.exit(f"{slug} is in the include list of both {included[slug]} and {p['name']}.")
            included[slug] = p["name"]
    result = {}
    for s in skills:
        slug, cat = s["slug"], s["category"]
        if slug in included:
            result[slug] = included[slug]
            continue
        claims = [p["name"] for p in plugins if cat in p.get("categories", []) and slug not in p.get("exclude", [])]
        if len(claims) > 1:
            sys.exit(f"{slug} (category {cat}) is claimed by {', '.join(claims)}.")
        if claims:
            result[slug] = claims[0]
    return result


def safe_path(folder, rel):
    full = os.path.normpath(os.path.join(folder, rel))
    if not full.startswith(folder + os.sep):
        raise RuntimeError(f"unsafe file path in the catalogue: {rel!r}")
    return full


def tree_digest(paths):
    h = hashlib.sha256()
    for base in paths:
        if os.path.isfile(base):
            h.update(base.encode())
            h.update(open(base, "rb").read())
            continue
        for dirpath, dirnames, filenames in sorted(os.walk(base)):
            dirnames.sort()
            for name in sorted(filenames):
                p = os.path.join(dirpath, name)
                h.update(os.path.relpath(p, ROOT).encode())
                h.update(open(p, "rb").read())
    return h.hexdigest()


def first_sentence(text, limit=170):
    text = " ".join(text.split())
    text = re.sub(r",? (on live data |from live data )?through the InsightfulPipe MCP(?=[ .,])", "", text)
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    sentence = m.group(1) if m else text
    if len(sentence) <= limit:
        return sentence
    cut = sentence[: limit - 1]
    return cut[: cut.rfind(" ")].rstrip(",;:") + "…"


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def sync_files(skill):
    data = fetch(f"{SITE}/api/skills/{skill['category']}/{skill['slug']}/files")
    folder = os.path.join(SKILLS_DIR, skill["slug"])
    os.makedirs(folder, exist_ok=True)
    keep = set()
    for f in data["files"]:
        raw = base64.b64decode(f["content"]) if f.get("encoding") == "base64" else f["content"].encode("utf-8")
        if f.get("sha256") and hashlib.sha256(raw).hexdigest() != f["sha256"]:
            raise RuntimeError(f"{skill['slug']}/{f['path']}: checksum does not match the catalogue")
        target = safe_path(folder, f["path"])
        os.makedirs(os.path.dirname(target), exist_ok=True)
        if not os.path.exists(target) or open(target, "rb").read() != raw:
            with open(target, "wb") as out:
                out.write(raw)
        keep.add(os.path.relpath(target, folder))
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            p = os.path.join(dirpath, name)
            if os.path.relpath(p, folder) not in keep:
                os.remove(p)


def page_cell(s):
    """A queued skill has no page on the site yet."""
    return "" if s.get("queued") else f"[Page]({PAGES}/{s['category']}/{s['slug']})"


def readme(p, skills):
    n = len(skills)
    repo = f"{ORG}/{p['repo']}"
    example = next((s["slug"] for key in ("account-audit", "audit") for s in skills if key in s["slug"]), skills[0]["slug"])
    rows = "\n".join(
        f"| [{cell(s['displayName'])}](skills/{s['slug']}/) | {cell(first_sentence(s['description']))} | {page_cell(s)} |"
        for s in skills
    )
    return f"""# {p['displayName']}

**{p['description'].format(n=n)}**

Most of these skills also work from reports you export and paste in, with no account needed. Skills that need numbers read them live from your accounts when the InsightfulPipe MCP is connected.

Part of the free [InsightfulPipe marketing skills library]({LIBRARY}). Skills with a **Page** link have a page with a sample run at [insightfulpipe.com]({p['homepage']}); newer ones get theirs soon.

## Install

### Claude Code

```
/plugin marketplace add {repo}
/plugin install {p['name']}@{p['name']}
```

### Any agent: Claude Code, Codex, Cursor and others

```
npx skills add {repo}
```

Add `--skill {example}` to install one skill.

### Claude.ai and Claude Desktop

Download a skill's ZIP from its page on insightfulpipe.com (the **Page** links below), or zip its folder from `skills/` if it has no page yet, then in Claude open **Customize > Skills**, choose **+ Create skill > Upload a skill** and pick the ZIP. Skills need code execution turned on.

## Skills ({n})

| Skill | What it does | |
|---|---|---|
{rows}

## Live data (optional)

Skills that read account data use the [InsightfulPipe MCP server](https://insightfulpipe.com/mcp-servers) when it's connected. Without it, each skill tells you which exports to paste in and works from those.

## What this plugin runs and sends

The plugin contains skills only: Markdown instructions (`SKILL.md`, `HOW_TO_USE.md`) and sample input and output files. It adds no hooks, commands or MCP servers, runs no code on your machine and sends no data anywhere by itself. When you have the InsightfulPipe MCP connected, Claude uses it to read your accounts, and makes a change only after you confirm it. The `scripts/` and `.github/` folders keep this repository in sync with insightfulpipe.com and are not part of what the plugin does.

## License

MIT. See [LICENSE](LICENSE).
"""


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
        out.write("\n")


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else json.load(open(PLUGIN))["name"]
    mapping = load_mapping()
    p = next((x for x in mapping["plugins"] if x["name"] == name), None)
    if not p:
        sys.exit(f"{name} is not in plugins.json.")
    catalogue = fetch(f"{SITE}/api/skills")
    every = catalogue.get("skills") or []
    if not every:
        sys.exit("The catalogue lists no skills; leaving the plugin as it is.")
    every = every + load_queued({s["slug"] for s in every})
    own = owners(mapping, every)
    skills = sorted((s for s in every if own.get(s["slug"]) == name), key=lambda s: s["displayName"].lower())
    if not skills:
        # A new plugin waits for its first released skill; that is not a failure.
        print(f"No published skill belongs to {name} yet; leaving the plugin as it is.")
        return

    os.makedirs(SKILLS_DIR, exist_ok=True)
    existing = {d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))}
    removed = existing - {s["slug"] for s in skills}
    if existing and len(removed) > MAX_REMOVED * len(existing):
        sys.exit(f"{len(removed)} of {len(existing)} skills would be removed; stopping without changes.")

    tracked = [SKILLS_DIR, README, LICENSE]
    before = tree_digest([t for t in tracked if os.path.exists(t)] + [p_ for p_ in (PLUGIN, MARKETPLACE) if os.path.exists(p_)])
    for s in skills:
        if s.get("queued"):
            sync_queued_files(s)
        else:
            sync_files(s)
    for slug in removed:
        shutil.rmtree(os.path.join(SKILLS_DIR, slug))
    with open(README, "w") as out:
        out.write(readme(p, skills))
    if not os.path.exists(LICENSE):
        with open(LICENSE, "w") as out:
            out.write(MIT)

    old = json.load(open(PLUGIN)) if os.path.exists(PLUGIN) else {}
    description = p["description"].format(n=len(skills))
    manifest = {
        "name": name,
        "displayName": p["displayName"],
        "description": description,
        "version": old.get("version", "1.0.0"),
        "author": {"name": "InsightfulPipe", "url": SITE},
        "homepage": p["homepage"],
        "repository": f"https://github.com/{ORG}/{p['repo']}",
        "license": "MIT",
        "keywords": p["keywords"],
    }
    market = {
        "name": name,
        "owner": {"name": "InsightfulPipe", "url": SITE},
        "metadata": {"description": description, "version": manifest["version"]},
        "plugins": [{"name": name, "description": description, "source": "./"}],
    }
    write_json(PLUGIN, manifest)
    write_json(MARKETPLACE, market)

    if tree_digest(tracked + [PLUGIN, MARKETPLACE]) != before:
        now = datetime.datetime.now(datetime.timezone.utc)
        version = f"{now.year}.{now.month}.{now.day * 100 + now.hour}"
        manifest["version"] = market["metadata"]["version"] = version
        write_json(PLUGIN, manifest)
        write_json(MARKETPLACE, market)
        queued = sum(1 for s in skills if s.get("queued"))
        print(f"Updated {name}: {len(skills)} skills, {queued} not on the site yet ({len(removed)} removed), version {version}.")
    else:
        print(f"No changes: {name}, {len(skills)} skills.")


if __name__ == "__main__":
    main()
