# How to Use This Skill

Hey Claude, I just added the "microsoft-ads-optimizer" skill. Find what to fix in my Microsoft Ads account and show me the exact changes before you make any.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Microsoft Advertising account added.** The skill reads the account itself; you don't export anything.
- **A Read & Write connection** if you want it to make the changes. With read-only access it still drafts every change for you to apply.
- **Your target CPA,** if you have one. Without it, the skill uses your account's own CPA. With no conversions at all, it skips the conversion-based rules and says so.
- **For a new campaign:** what you're advertising, the landing page, the daily budget and where to show the ads.

## Example requests

**Clean up an account**
Hey Claude, I just added the "microsoft-ads-optimizer" skill. Find the search terms wasting money in my Microsoft Ads account and draft the negative keywords. Don't add anything yet.

**Pause what isn't working**
Hey Claude, I just added the "microsoft-ads-optimizer" skill. Which keywords should I pause in my Bing Ads account? My target CPA is $60.

**Budgets**
Hey Claude, I just added the "microsoft-ads-optimizer" skill. Check my Microsoft Ads campaign budgets and tell me which ones to raise or cut, with the change you'd send.

**New campaign from a brief**
Hey Claude, I just added the "microsoft-ads-optimizer" skill. Build a new Microsoft Ads search campaign for our project management software at $30 a day, with keywords and a responsive search ad. Copy the locations from my current campaign and keep everything paused.

**Fix, then launch**
Hey Claude, I just added the "microsoft-ads-optimizer" skill. Find what to fix in my Microsoft Ads account and draft a new search campaign for our invoicing software at $20 a day. Show me the changes first.

## What you get

1. **A header** with the date window, the time zone and whether your conversion tracking works. If nothing ran in the last 30 days, it looks back a full year and labels the findings as history.
2. **Negative keywords** taken from your own search terms, grouped by what the searcher wanted, with the spend behind each one. Terms that match what you sell go on a watch list instead.
3. **Keywords to pause,** with the rule each one breaks and its numbers.
4. **Budget changes,** including a minimum daily budget worked out from your own cost per click.
5. **Responsive search ad checks,** and new ads with every headline counted against Microsoft's 30-character limit and tagged with where it came from.
6. **A new campaign** if you ask for one: campaign, locations, ad group, keywords, ad and negatives.
7. **A change list:** every change as the exact request it would send, marked not run, ask first or conditional.

## What it can change for you

With your yes on the exact change, it can:
- add negative keywords to a campaign, an ad group or a shared negative list
- pause keywords
- change a campaign budget or a shared budget
- add a responsive search ad (created paused), then turn it on after you've reviewed it
- create a new search campaign with its locations, ad group, keywords, ad and negatives, all paused

It never changes bids or bid strategies, and it never deletes anything.

## Tips

- Fix conversion tracking first if the skill says it's unverified. Until then, pauses and budget raises can only be judged on relevance, not results.
- Run it again two to four weeks after the changes, once the new negatives and budgets have had time to work.
- New campaigns stay paused until you turn them on. Look them over in Microsoft Advertising first.
