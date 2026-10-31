# How to Use This Skill

Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Look up my three biggest competitors in the TikTok ad library, pull the TikTok top ads for my category, and tell me what to test next.

## What you need

- **Nothing connected, if you prefer.** Paste the links of competitor ads you found on library.tiktok.com or in TikTok Creative Center, with what the page shows (advertiser, caption, first and last shown dates, reach band, landing page), plus an ad-level export from TikTok Ads Manager. The skill runs the same analysis on what you paste.
- **Or the InsightfulPipe MCP connected to Claude, with the Ad Libraries source added.** The skill then searches the TikTok Ad Library and Creative Center Top Ads itself.
- **Your TikTok Ads account,** connected the same way, if you want your own ads compared with theirs. Optional.
- **Your competitors:** up to 4, with the brand name, the legal company name if you know it, the website and the TikTok handle. The Library lists advertisers by legal name, and the website and handle are how the skill confirms an ad is really theirs.

## Example requests

**Named competitors in Europe**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Search the TikTok ad library for Northpeak Apparel and Kinetiq Wear in the UK and Germany over the last 90 days. Which of their ads have run longest?

**Category top ads**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Show me the TikTok top ads for apparel in the US this month, with their hooks and video lengths.

**Side by side with my account**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Compare my TikTok ads with what my competitors run: hooks, formats, landing pages and CTAs.

**Swipe file**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Build me a TikTok swipe file of competitor hooks, grouped by angle, with a link to every ad.

**Where they advertise**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Which European countries and age groups is this competitor targeting on TikTok?

**From pasted links**
Hey Claude, I just added the "tiktok-competitor-ads-research" skill. Here are 10 TikTok ad library links for two competitors and my Ads Manager export. What are they doing that I'm not?

## What you get

1. **A snapshot:** each competitor's own ads in the Library, how many are still showing, how many are proven (still showing after 30 days or more), the widest reach band, and how many posts by other accounts mention them, counted but never named.
2. **Run length:** each competitor's five longest-running ads, with a Library link.
3. **Hooks and angles:** the opening line of every caption and the angles each caption uses, with up to two exact quotes per angle, each the line that shows it.
4. **Format and length:** video vs image per competitor, and the video length mix of the category's top ads.
5. **Landing pages, CTAs and objectives** for each competitor's best ads, beside yours.
6. **Targeting:** the countries, ages and genders each competitor targets, and where their impressions land.
7. **A category benchmark** from Creative Center Top Ads, ranked by TikTok's CTR rank.
8. **Your own ads beside theirs:** hook rate, hold rate, CTR and cost per result, compared only within one optimization goal.
9. **What to test next:** three to five ideas, each with the ads behind it.
10. **The gaps:** what each source couldn't show.

Every finding is tagged with its source: `[Library]`, `[Top Ads]` or `[Your account]`.

## What it can change for you

Nothing. The ad library and Top Ads are public and read only, and the skill only reads your TikTok Ads account.

## Tips

- The TikTok Ad Library only lists ads shown in the EU, EEA, UK, Switzerland and Turkey. A competitor that advertises only in the US shows nothing there; use Top Ads for the US.
- A search in the Library matches caption text as well as advertiser names, so most results for a known brand are other people's posts about it. Give the legal company name, website and handle so the skill keeps only the brand's own ads.
- Neither source shows spend. A long run is a good sign an ad works, not proof.
- For the Meta, Google, Microsoft and LinkedIn libraries, run `competitor-ad-research` in the same chat, if you have it installed. Both snapshots count ads found, ads still running and advertiser names, so those columns can sit side by side.
