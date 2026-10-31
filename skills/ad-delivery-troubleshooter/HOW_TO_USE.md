# How to Use This Skill

Hey Claude, I just added the "ad-delivery-troubleshooter" skill. My new campaigns on LinkedIn, TikTok and Microsoft Ads have barely spent since Monday. Find out why and tell me what to fix first.

## What you need

- **Either screenshots or a connection.** Without a connection, share screenshots of the campaign, ad group and ad rows with the status columns showing, plus any error or hover text. With the InsightfulPipe MCP connected, the skill reads the statuses, review results, budgets, bids and schedules itself.
- **The campaigns that are stuck,** their launch date and the budget you expected them to spend.
- **The audience size estimate** from the targeting panel, if you have it. Most platforms don't return it through their API.

## Example requests

**TikTok ads not delivering**
Hey Claude, I just added the "ad-delivery-troubleshooter" skill. My TikTok ad group has been active for two days and shows no impressions. Here's a screenshot of the ad group and ad rows.

**LinkedIn ads not spending**
Hey Claude, I just added the "ad-delivery-troubleshooter" skill. My LinkedIn campaign has an $80 daily budget and spends about $6 a day. Check it through my connected account.

**Microsoft Ads no impressions**
Hey Claude, I just added the "ad-delivery-troubleshooter" skill. One of my Microsoft Ads ad groups gets no impressions at all. Is it the ads, the keywords or the bid?

**Reddit, from screenshots**
Hey Claude, I just added the "ad-delivery-troubleshooter" skill. My Reddit campaign is stuck. Here are screenshots of the campaign, the ad and the billing page.

## What you get

1. **A verdict for each campaign:** stopped, throttled or delivering, with its budget, its actual daily spend and the share.
2. **The causes in order,** each marked confirmed, likely or possible, with the exact status, setting or screenshot that shows it and the fix.
3. **What was ruled out,** so you don't recheck it.
4. **What's still needed** to settle the open causes, such as a billing or pixel screenshot.
5. **When to check again,** and which number should move.

## What it can change for you

With your yes on the exact change, and a Read & Write connection, it can:
- raise a LinkedIn bid into the suggested range or raise its daily budget
- fix a TikTok ad group's budget, bid or start date
- raise a Microsoft Ads ad group bid

It never switches a paused or rejected item on, never rewrites ads to get past review, and never touches billing.

## Tips

- Run it after the first full day; under 24 hours, most campaigns simply haven't ramped yet.
- Include every status hover text you see. The exact wording often names the cause.
- For Google Ads or Meta campaigns, use the Google Ads or Meta delivery skills instead.
