# How to Use This Skill

Hey Claude, I just added the "chatgpt-ads-analyzer" skill. How are my ChatGPT ads doing over the last 30 days, and what should I fix first?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your OpenAI Ads (ChatGPT Ads) account added.** The skill pulls the data itself; you don't need to export anything.
- **Your goal and target CPA or ROAS,** if you have them. Without them, the skill reads your campaigns' bidding type and grades against your own average.
- **For the Google comparison:** your Google Ads account for the same business, connected in the same workspace.

## Example requests

**Account overview**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Give me an overview of my ChatGPT Ads account for the last 30 days compared with the 30 days before.

**Campaigns, ad groups and ads**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Which ChatGPT campaigns, ad groups and ads are pulling their weight, and which ones are wasting money?

**Pixel and conversions**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Is my OpenAI pixel working? Check my conversion events and tell me my CPA and ROAS by campaign.

**Audiences and lead forms**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Review my custom audiences and lead forms in ChatGPT Ads.

**ChatGPT vs Google**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Compare my ChatGPT Ads with my Google Search Ads for last month.

**Budget pacing**
Hey Claude, I just added the "chatgpt-ads-analyzer" skill. Are my ChatGPT campaigns on pace with their lifetime budgets?

## What you get

1. **A scorecard for nine areas:** account overview, campaigns, ad groups and ads, conversions, pixel and events, custom audiences, lead forms, the Google Search comparison, and budget pacing. Each is graded pass, warn, fail or not graded.
2. **The top 5 findings,** failures first, each with the call and the numbers behind it and who can fix it.
3. **Detail tables** for campaigns, ad groups and ads, conversions, pixels and event settings, audiences and pacing.
4. **A plain list of what couldn't be graded,** and why: for example no delivery yet, or lead tools not switched on for your account.

## What it can change for you

With your yes on the exact change, it can:
- raise or lower a campaign's lifetime budget
- pause a campaign or an ad
- change an ad group's max bid

It never switches a campaign, ad group or ad on, and it never archives, because archiving deletes for good. If a campaign has hit its lifetime budget, it tells you before you confirm that raising the budget makes it spend again.

## Tips

- If nothing has delivered yet, the skill still checks your pixel, event settings, audiences and ad review status. That's usually where the reason is.
- Fix the pixel before you judge CPA. ChatGPT Ads counts conversions only from the pixel and the Conversions API.
- Lead forms are switched on by OpenAI per account. When they're off, the report says so instead of showing zeros.
