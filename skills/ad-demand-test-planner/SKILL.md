---
name: ad-demand-test-planner
description: Plans and reads a paid smoke test on Google Search, Meta, LinkedIn or Reddit that checks demand, a message or a price before you build, with pass and kill lines, budget and a waitlist page brief. Use when validating a business idea with ads, testing product demand or sizing a demand test.
---

# Ad Smoke Test Planner

A smoke test buys a few hundred visits to a page for an offer that isn't built yet and counts how many people ask for it. Done loosely it buys noise: too few visits to read, a budget picked out of the air, and a "success" line chosen after the results are in. This skill fixes the numbers before the first dollar is spent and reads the result against them.

It has two modes, and runs both when the user asks for the whole thing:

- **Plan** a test: one offer (a demand test) or two to four promises or prices for the same offer (a message test).
- **Read** a finished test against the rule frozen in the plan.

It decides the test, not the business. Whether to build the product, across interviews, pre-orders and this test, is a bigger call; hand it to `idea-validation-plan` if installed.

## Before you start

Ask for what only the user knows, and use the defaults when they don't know:

1. **The offer:** what it does, who buys it, the price, and the country and language.
2. **What the test decides,** in one sentence: "If ..., we build it / lead with that message; if not, we ...".
3. **Most they'll pay to win one customer.** Default: one third of the first year's gross profit per customer (price x 12 x gross margin / 3). Say it's a default.
4. **Sign-up-to-customer rate:** of the people who join the waitlist, how many would buy. Default: 10%. Use their own number from a past waitlist or launch when they have one.
5. **Budget cap and the latest decision date.**
6. **For a message test:** the two to four promises or prices. If they have none, write them (see "Variants").

Then work out the one number everything hangs on:

**Allowed cost per sign-up = most they'll pay per customer x sign-up-to-customer rate.** At $150 and 20%, that's $30.

If the InsightfulPipe MCP is connected, call `query_contexts` with `request="accounts"` for `google-ads`, `facebook-ads`, `linkedin-ads` and `google-analytics`, and `request="actions_details"` for the actions named below. Follow the body shapes it returns. Without a connection, ask the user to paste the same numbers (Keyword Planner rows, a past campaign's CPC, Meta's audience estimate); the method doesn't change.

## Step 1: cost and reach per channel

For each channel, find the cost per click, how many clicks become page visits (the land rate), and whether the channel can reach enough people in the run time. **Cost per visit = CPC / land rate.**

**Land rate.** Use the account's own: GA4 sessions from that source and medium / the platform's link clicks over the last 90 days. With no history, use 85% and replace it with the real figure at the readout.

### Google Search

Call `generate_keyword_ideas` (google-ads) with two or three seed phrases, the country and the language. It returns `avg_monthly_searches`, `low_top_of_page_bid` and `high_top_of_page_bid`.

- **Build the test set:** phrases a buyer of this offer would type. Leave out, with a reason each: category terms that mean a whole product the user doesn't sell, phrases asking for a no-cost tool, rival brand names, jobs, how-to and definitions.
- **CPC** = the searches-weighted average of each phrase's (low + high) / 2.
- **Reach ceiling** = test set searches a month x run days / 30 x 10%. Ten percent is a generous click share for a new ad, on purpose: if even that can't buy the visits needed, Search can't run this test.

Search can test demand. It splits messages badly, because one keyword serves one ad at a time and Google rotates ads unevenly. For a message test on Search, run one ad and split the page instead (each visitor sees one headline at random).

### Meta

1. `search_interests` (facebook-ads) for the buyer's interests; note the ids.
2. `estimate_audience_size` with the targeting spec; read `users_lower_bound`.
3. `get_insights_adaccount` at `level` `ad` for the last 90 days with `spend`, `inline_link_clicks` and `impressions`. **CPC** = spend / link clicks, and **link CTR** = link clicks / impressions, when the account had 1,000 or more link clicks. Otherwise use the user's own number, or plan with a stated guess and recheck after two days of spend before freezing the plan.
4. `get_minimum_budgets`: the USD row's `min_daily_budget_high_freq` is the floor per ad set when optimising for clicks or landing page views. Values are in cents.
5. **Frequency check:** planned impressions = clicks needed / link CTR. If that's more than 3 impressions per person in the audience's lower bound, widen the audience or cut variants.

### LinkedIn

Call `get_budget_pricing` (linkedin-ads) with `bid_type` CPC, `campaign_type` SPONSORED_UPDATES, `match_type` EXACT and the targeting (job titles, functions or industries, and location). Use `suggestedBid.default` as the CPC and `dailyBudgetLimits.min` as the floor.

### Reddit

There's no Reddit Ads connector. Use a CPC the user pastes from a past Reddit campaign; without one, mark Reddit "not costed" rather than guess.

## Step 2: the lines, per channel

Each channel gets its own lines, because each has its own cost per visit:

- **Pass line** = cost per visit / allowed cost per sign-up. At $1.73 a visit and $30 allowed, 5.77% of visitors must sign up for the test to pay its way.
- **Kill line** = pass line / 2. A finished launch page, better targeting and a few weeks of learning can plausibly double a smoke test's rate. Below half the line, nothing plausible rescues it. The user can set a different kill line before launch, never after.
- **If the pass line is above 25%,** reject the channel: cold paid traffic doesn't sign up at that rate. Say what would need to change (a higher allowed cost, a cheaper channel).

## Step 3: visits, budget and run time

**Visits per variant** (one-sided 95% confidence, 80% power, kill line k against pass line p):

n = ((1.645 x sqrt(k(1 - k)) + 0.8416 x sqrt(p(1 - p))) / (p - k))^2, rounded up.

- **Total visits** = n x number of variants. A demand test has one variant.
- **Budget** = total visits x cost per visit x 1.15. The 15% covers costs drifting up during the run.
- **Run time:** 14 days by default, so every weekday shows up twice. Never under 7. If it needs more than 21 days, cut variants first.
- **Daily budget per variant** = budget / variants / run days. It must clear the platform's floor.
- **The detectable gap.** Show how far apart two variants must be before the test can call one better: (z + 0.8416) x sqrt(2p(1 - p) / n), where z is the two-sided critical value at 0.05 / (variants - 1). Gaps smaller than that will read "not proven", and the user should know it before paying.

**Pick the channel:** of the channels whose pass line is 25% or under, whose reach covers the clicks needed, and whose budget fits the cap, take the cheapest. Run one channel per test. A second channel is a second test with its own lines.

**If nothing fits,** in this order: cut to two variants, then one; ask whether the allowed cost per customer can honestly go up; otherwise don't run a paid test. Say so plainly and point to buyer conversations or a pre-sale instead (`idea-validation-plan` if installed).

## Step 4: variants and setup

**Writing variants.** Two to four. Each one changes one thing: the promise (the problem it solves or the result it gives), or the price shown. Everything else stays the same: the audience, placements, image or video, call to action and page template. A price test shows the same promise at different prices.

**Setup on Meta or LinkedIn:**
- One campaign. One ad set (Meta) or one campaign per variant inside a campaign group (LinkedIn), each with its own equal daily budget. Never a shared campaign budget: delivery would pour money into whichever variant gets the first few clicks.
- On Meta, optimise for landing page views (or link clicks), not leads, so delivery doesn't chase sign-ups differently per variant.
- Each ad links to the page with `?v=<letter>` and `utm_source=<platform>&utm_medium=paid&utm_campaign=smoke-<offer>&utm_content=<letter>`; the page shows the matching headline.

**Source of truth.** Count sign-ups on the site: a GA4 key event fired on the thank-you state, or the form tool's list. Platform-reported leads can include view-through credit and repeat submits.

**Before launch,** submit one test sign-up on each page version and confirm it reaches GA4.

## Step 5: the page brief and the honest note

**Page brief, per variant:**
- Above the fold: the variant headline, one line on what it does, the real intended price, and the button ("Join the waitlist" or "Reserve a spot").
- A status line next to the button: "Coming soon. We're building this now and will email you when it opens."
- Form: email plus at most one qualifying field.
- Visuals: a design mock-up labelled as a preview, never a screenshot that suggests it works today.

**The honest note.** People who sign up are told the truth straight away:
- **Thank-you page and confirmation email:** it isn't available yet, they're helping decide what gets built, they'll hear once when it opens or if it won't be built, and no payment has been taken.
- **Ad copy** says "coming soon" or "join the waitlist". Nothing says or implies it can be bought or used today. Ads that promise what people can't get break Google's misrepresentation policy and Meta's advertising standards, and can get the account restricted.
- **Money:** take none for something with no date. A deposit is only fine when it's fully refundable and the page states the expected date.
- **Follow-up:** write the date by which every sign-up hears the outcome, and keep it.

## Step 6: freeze the rule

Write this down before launch and don't change it after:
- the visits per variant, the budget, the end date
- the pass line, kill line and allowed cost per sign-up
- the source of truth for sign-ups
- the outcomes below
- no early stop for good news; stop early only if tracking breaks or spend reaches the cap

## Reading the test

**Pull the results** for the test window:
- **Spend and clicks per ad:** `get_insights_adaccount` (facebook-ads, `level` `ad`, `spend`, `inline_link_clicks`, `impressions`, `actions`), `ad_performance_report` (google-ads), or `get_creative_analytics` (linkedin-ads, `clicks`, `impressions`, `costInUsd`).
- **Visits and sign-ups:** `get_report` (google-analytics) with dimensions `sessionCampaignName` and `sessionManualAdContent` and metrics `sessions` and `keyEvents:<sign-up event>`. Keep only the test campaign's rows; say which rows you left out.
- No connection: ask for spend, clicks, visits and sign-ups per variant.

**Per variant:**
- Visits = GA4 sessions; sign-ups = the key event (or the form list).
- Sign-up rate, with a 95% Wilson interval.
- **Critical rate** = k + 1.645 x sqrt(k(1 - k) / visits), with k the kill line.
- Actual cost per visit and per sign-up.
- Land rate = visits / clicks. If a variant's land rate is under 80% of the variants' average, its page version lost visitors (slow load, broken link); fix it and rerun that variant before trusting its rate.

**Outcome per variant:**

| Outcome | When |
|---|---|
| **Go** | rate at or above the pass line, and actual cost per sign-up at or under the allowed cost |
| **Real but short** | rate at or above the critical rate, but not a go: real interest, not at a price that pays. Change the price, page or audience; don't scale |
| **Stop** | rate under the critical rate: the test can't tell it apart from the kill line |
| **Not read** | fewer visits than planned and budget left: run on to the planned visits |

**Which message won.** Compare the leader with each other variant using a two-proportion z-test, two-sided, at 0.05 / (variants - 1). Below that p-value it's "proven better"; above, "not proven", even when the rates look far apart. A variant can be a go without being proven better than the runner-up; say which one the decision rests on.

## The report

**Plan:**
1. The decision sentence and the allowed cost per sign-up, with the math.
2. A channel table: CPC and its source, land rate and its source, cost per visit, pass and kill lines, visits needed, budget, reach check, verdict and why.
3. The sizing for the chosen channel: visits per variant, total, budget, run dates, daily budget per variant against the floor, and the detectable gap.
4. The variants and setup, with each ad's link.
5. The page brief and the honest note, word for word.
6. The frozen rule.
7. What couldn't be checked, and why.

**Readout:** one row per variant (spend, clicks, visits, land rate, sign-ups, the platform's own lead count, rate, interval, critical rate, cost per sign-up, outcome), the pairwise results, the checks, three or four findings with their numbers, the decision on the test, and what it doesn't prove.

## Fixes this skill can run

None. It plans and reads; it never creates, launches, pauses or edits a campaign, and never touches the page. To build the campaigns from the plan, use `facebook-ads-campaign-structure`, `google-ads-campaign-builder` or `linkedin-ads-campaign-builder` if installed, and `facebook-ads-launch-checklist` before a Meta test goes live.

## Rules

- Lines, visits and budget are fixed before launch. Never move a line after seeing results.
- One channel per test; one change per variant.
- Every cost and reach figure names its source: a call, the account's own history, the user, or a stated default.
- An honest empty result beats a guess: a channel with no costs is "not costed".
- No ad or page claims the offer exists today.
- Sign-ups are interest, not revenue. Say what the go still rests on (usually the sign-up-to-customer rate) and how to check it.

## Go deeper

If installed: `idea-validation-plan` (the build or stop call across all the evidence), `ab-test-designer` (tests on a live page with existing traffic), `creative-testing-roadmap` (ongoing creative tests once the offer is live), `landing-page-auditor` (the waitlist page) and `copywriting` (the variant headlines).
