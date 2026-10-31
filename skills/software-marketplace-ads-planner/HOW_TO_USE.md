# How to Use This Skill

Hey Claude, I just added the "software-marketplace-ads-planner" skill. We ran Capterra PPC in three categories for the last 60 days. Review it against GA4, then plan the next 60 days, including whether G2 Clicks is worth testing.

## What you need

- **What counts as a signup** (a trial start, a demo request, or an install), and your target cost per signup. No target? Give your first-year revenue per new customer and your signup-to-paid rate, and the skill works one out.
- **The categories you bid on or want to,** with the directory and whether each is your main category or a side one.
- **What the vendor portal shows** for each category: minimum bid, any bid shown for the top positions, monthly minimum, or the price of a fixed-term placement. The skill never guesses a directory's prices.
- **Each category page,** pasted or as a screenshot: the first five listings with review count, rating and whether they are sponsored. Directory pages block automated reading, so this is always a paste.
- **Your listing's review count and rating** on each directory, and the page each category sends clicks to.
- **For a review,** the directory's report by category: clicks, spend, average position and the conversions it reports.
- **Optional, through the InsightfulPipe MCP:** GA4 for signups from each directory and category by UTM, Search Console for how much Google search each category's words get, and the site crawler to read each destination page. Without them, paste the same numbers.

## Example requests

**Plan before spending**
Hey Claude, I just added the "software-marketplace-ads-planner" skill. Are Capterra ads worth it for us? We sell project management software for agencies, our target is $120 per demo, and here are the three category pages and what the portal shows for bids.

**Review a running campaign**
Hey Claude, I just added the "software-marketplace-ads-planner" skill. Here is our Capterra PPC report for September. Match it to GA4 signups by category and tell me which categories to keep, lower, or stop.

**G2 sponsored listings**
Hey Claude, I just added the "software-marketplace-ads-planner" skill. G2 quoted us a quarterly sponsored placement on two category pages. Here is the quote and both category pages. Can our listing compete there, and how many clicks would the placement need to deliver to be worth it?

**App marketplace ads**
Hey Claude, I just added the "software-marketplace-ads-planner" skill. We run Shopify App Store search ads. Here is the Partner Dashboard export by keyword and our install-to-paid rate. What should we bid on each keyword?

## What you get

1. **A target cost per signup** with the math shown.
2. **The highest bid each category can pay,** from your own signups per click.
3. **A compete check** of your review count and rating against the top five listings on each category page you paste.
4. **A destination check** for each category: does the page name the category, match the listing's button and show prices.
5. **A verdict for each category:** bid, skip or fix listing first before launch; keep, lower bid, fix listing, stop or too early once it runs.
6. **The next period's budget, tagged links and a stop rule** with a review date, written before the money goes out.

## What it can change for you

Nothing. There is no directory connector, so you change bids, budgets and destination URLs in the vendor portal. The skill gives you the exact values for each category.

## Tips

- Tag every category's destination with its own `utm_campaign`, so GA4 can tell categories apart.
- Judge on the signups GA4 records. A directory's own conversion count is useful context, not the verdict.
- Fix a listing that fails the compete check before you buy clicks for it. Reviews move the comparison more than bids do.
- Run the review at the date the plan sets, and apply the stop rule as written.
