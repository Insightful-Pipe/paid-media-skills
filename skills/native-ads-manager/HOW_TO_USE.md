# How to Use This Skill

Hey Claude, I just added the "native-ads-manager" skill. Here are my Taboola and Outbrain exports for the last two weeks. Tell me which sites to block or boost, check my tracking, and write my next headline test.

## What you need

- **Your network exports** for the same dates (the last 14 complete days works best):
  - Taboola: the By Site report and the Top Campaign Content report.
  - Outbrain: the Sections report and the Ads report.
  - Spend, clicks and conversions per campaign for each of the two weeks.
- **Each campaign's tracking code,** pasted as text.
- **Your target cost per conversion,** if you have one. Without it, the skill uses each campaign's own average.
- **Optional: the InsightfulPipe MCP with GA4 connected,** so the skill can check which sites send people who actually reach and use your page. If your exports sit in a Google Sheet, connect Google Sheets and the skill reads them there.

## Example requests

**Weekly read**
Hey Claude, I just added the "native-ads-manager" skill. Here is my Taboola By Site report for the last 14 days. Which sites should I block, and which should get a higher bid? My target CPA is $60.

**Accidental clicks**
Hey Claude, I just added the "native-ads-manager" skill. My Taboola clicks don't match my GA4 sessions. Use GA4 to find the sites that send clicks nobody follows through on.

**Headline test**
Hey Claude, I just added the "native-ads-manager" skill. Here is my Outbrain Ads report. Find what my best headlines have in common and write the next test grid.

**Tracking check**
Hey Claude, I just added the "native-ads-manager" skill. Check this Outbrain tracking code and tell me why GA4 can't see which sections my visitors came from.

**Launch plan**
Hey Claude, I just added the "native-ads-manager" skill. I want to start Taboola ads for my online store. Write the campaign plan, the first headlines and the brief for the presell page.

## What you get

1. **A verdict for every site or section:** block, bid down 20%, keep or boost 20%, with the numbers behind it. Sites with too few clicks get no verdict until they have enough.
2. **The block list and bid changes,** ready to enter in each network.
3. **An accidental clicks check** from GA4: sites whose clicks don't reach your page or don't engage.
4. **A headline and thumbnail read** from your own item report, with the patterns, the flags and a 10-item test grid.
5. **A tracking check** with the corrected tracking code, and a comparison of the network's conversions with GA4's.
6. **For a new campaign:** the setup, a budget to learn on, the first grid and the presell page brief.

## What it can change for you

Nothing in Taboola or Outbrain: there is no connection to them. You enter the block list, bid changes, tracking code and new ads yourself. It only reads GA4 and Google Sheets.

## Tips

- Run it once a week on a rolling 14 days. Move each site one step per week.
- Fix the tracking code first if the check fails. The accidental clicks check needs the site name in your GA4 data.
- For the full presell page, use the advertorial-presell-writer skill, if you have it, with the brief this skill writes.
