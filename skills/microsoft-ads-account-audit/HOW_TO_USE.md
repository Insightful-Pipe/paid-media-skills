# How to Use This Skill

Hey Claude, I just added the "microsoft-ads-account-audit" skill. Audit my Microsoft Ads account and tell me what to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Microsoft Ads account added.** The skill pulls the data itself; you don't need to export anything.
- **Your target CPA or ROAS,** if you have one. Without it, the skill uses your own average for the period.
- **Your Google Ads account, connected too,** if you want the Google import gap check or the Microsoft vs Google CPC comparison. It must be the same business.

## Example requests

**Full audit**
Hey Claude, I just added the "microsoft-ads-account-audit" skill. Run a full audit on my Microsoft Ads account for the last 30 days. My target CPA is $60.

**After a Google Ads import**
Hey Claude, I just added the "microsoft-ads-account-audit" skill. We imported our Google Ads campaigns into Microsoft Ads last month. Check what the import missed and compare our CPCs on both.

**Restarting a paused account**
Hey Claude, I just added the "microsoft-ads-account-audit" skill. Our Microsoft Ads have been paused since spring. Audit the account and tell me what to fix before we turn it back on.

**Monthly summary for a client**
Hey Claude, I just added the "microsoft-ads-account-audit" skill. Give me a one-page executive summary of last month's Microsoft Ads results, with the trend and the top fixes.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A short executive summary** and a month-by-month trend table.
3. **A scorecard for eight areas:** measurement (UET tags and conversion goals), wasted spend, structure and Google import gaps, keywords and Quality Score, ads and extensions, bidding, budget and impression share, networks, devices, locations and schedule, and other campaign types (Shopping, Performance Max, Audience).
4. **The top 5 fixes.** For a live account they're ranked by the money at stake each month. For a paused account they're a relaunch checklist.
5. **A list of what couldn't be checked,** and why.

If the account had no spend in the last 30 days, the skill still checks every setting, then reviews the most recent months that had spend and marks those findings as historical.

## What it can change for you

With your yes on the exact change, it can:
- add negative keywords taken from your own search terms
- attach sitelinks or callouts you already have to a campaign
- add new sitelinks or callouts

It never changes budgets, bids, bid strategies, locations, networks or conversion goals.

## Good to know

- Microsoft's Recommendations tab, the Professional Demographics (LinkedIn profile) report and the Product Dimension (Shopping item) report aren't available through the connector. Paste an export and the skill works it into the audit.
- Hour-of-day data only goes back 6 months in Microsoft Ads.
- Run it monthly, and again after any big change to tracking or campaign structure.
