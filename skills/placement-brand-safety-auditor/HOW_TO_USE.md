# How to Use This Skill

Hey Claude, I just added the "placement-brand-safety-auditor" skill. Check where my ads ran outside the main feeds last month and give me a block list for each platform.

## What you need

- **The site and app reports from each platform,** as CSV, XLSX or a paste: the TikTok Ad Network delivery report (Tools > TikTok Ad Network brand safety), the Microsoft Advertising Website URL (publisher) report, the LinkedIn Audience Network report from Campaign Manager, or your DSP's domain and app report. Platforms report their partner networks as one total, so the per-site and per-app detail comes from these.
- **Your current block lists,** so the new lists add to them instead of replacing them.
- **Your red lines:** the content your brand must never appear next to.
- **Your target cost per result** on each platform, if you have one. Without it, the skill uses each platform's main-feed cost per result.
- **Optional: the InsightfulPipe MCP** with TikTok Ads, Microsoft Advertising, LinkedIn Ads and GA4 connected. Then the skill pulls the network splits, ad group and campaign settings, and visit quality itself.

## Example requests

**Full audit across platforms**
Hey Claude, I just added the "placement-brand-safety-auditor" skill. Audit our TikTok, Microsoft and LinkedIn partner networks for the last 30 days. Our red lines are kids' apps, gambling and crime news. Target cost per lead is $60.

**TikTok Ad Network (Pangle) only**
Hey Claude, I just added the "placement-brand-safety-auditor" skill. Here's our TikTok Ad Network delivery report. Which apps are sending junk clicks, and should Pangle stay on in each ad group?

**Microsoft Audience Network**
Hey Claude, I just added the "placement-brand-safety-auditor" skill. Here's the Website URL report from Microsoft Ads. Find the sites to exclude and tell me if Audience ads should stay on in my Search campaigns.

**LinkedIn Audience Network**
Hey Claude, I just added the "placement-brand-safety-auditor" skill. Should LinkedIn Audience Network stay on in my campaigns? Here's the publisher report. Build the block list for Campaign Manager.

**DSP brand safety check**
Hey Claude, I just added the "placement-brand-safety-auditor" skill. Here's our DSP domain report with viewability and invalid traffic. Which sites look made for advertising, and which put us next to unsafe content?

## What you get

1. **A verdict for each partner network** in each ad group or campaign: turn it off, keep it with a block list, or keep it, with its cost per result next to the main feed's.
2. **Every site and app judged,** with the numbers and the flag behind each call: no return, accidental taps, thin visits, suspected made for advertising, costly, red line, or check by hand.
3. **A block list for each platform,** merged with your current list, in the format that platform takes.
4. **The setting changes,** and who makes each one.
5. **The money at stake** in the window, with any estimated figure labelled.
6. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, and a Read & Write connection, it can:
- update the TikTok Ad Network (Pangle) block list
- set site exclusions on a Microsoft Advertising campaign
- turn LinkedIn Audience Network off on a campaign

It shows the full change first, and it always sends your current list plus the new entries. Placement choices, inventory filters, LinkedIn and DSP block list uploads, budgets and bids stay as recommendations.

## Tips

- Add the placement to your ad URLs so GA4 can show whether partner clicks turn into real visits: `__PLACEMENT__` on TikTok, `{Network}` on Microsoft, and your DSP's site macro. LinkedIn has no placement macro.
- Run it monthly. Blocking a site stops future delivery there, and the platform may move the budget to other partner inventory.
