# How to Use This Skill

Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Draft a ChatGPT Ads campaign for my landing page, US only, bidding on clicks, with a $500 lifetime cap and a $3 max CPC. Show me the payloads before you create anything.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your OpenAI Ads (ChatGPT Ads) account added.** The skill reads the account itself; you don't need to export anything.
- **A brief:** the offer, the landing page, the countries, the goal (reach, clicks or conversions), a lifetime spend cap and a max bid.
- **A square image URL** for the ad card, at least 256 × 256.
- **Optional:** a customer list for an audience, the conversion you care about (sign-ups, leads, purchases), and whether you want a lead form.

## Example requests

**A new campaign**
Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Build a ChatGPT Ads campaign for our pricing page in the US and Canada, optimised for clicks, $1,000 lifetime cap, $2.50 max CPC.

**Add to a campaign that's running**
Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Add an ad group with three ads to my "Spring launch" campaign, aimed at people comparing project management tools.

**Ad copy only**
Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Write three ChatGPT ad variations for each of my ad groups, using only claims from the landing page.

**Tracking and audiences**
Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Set up the OpenAI pixel and a sign-up event, then build an audience from the customer list I'll paste.

**Lead form**
Hey Claude, I just added the "chatgpt-ads-campaign-builder" skill. Create and publish a demo request lead form for my ChatGPT Ads account.

## What you get

1. **A preflight of your account in 7 checks:** account review, landing page, name clashes and test clutter, a bid anchor from your own spend history, measurement, audiences and lead forms.
2. **The plan:** the campaign, one ad group per intent with 5 to 10 context hints, and 3 chat card ads per group with character counts and the page line behind each claim.
3. **Measurement, audience and lead form:** what will be reused, what will be created, and anything your account doesn't allow yet.
4. **Every create as an exact payload, in run order,** marked not run until you approve it.
5. **Open questions** the skill needs answered before the payloads are final.

## What it can change for you

With your yes on the exact payloads, it can:
- upload the ad image, and create the campaign, ad groups and ads (all created paused)
- create a preview link for an ad
- create a pixel and a conversion event
- create a custom audience and upload hashed identifiers from your list
- create and publish a lead form, where your account has lead forms enabled

Going live is a separate yes, and only after OpenAI has approved the ads. It never archives anything and never touches campaigns you didn't name.

## Tips

- Give one landing page per ad group. The copy can only claim what that page says.
- If you want conversion bidding, set up the pixel first and let it receive events. Bidding type can't be changed after the campaign is created.
- Lead forms need an entitlement OpenAI hasn't enabled on every account. The skill tells you if yours is missing it.
- Once the campaign has run for a while, a performance skill such as `chatgpt-ads-analyzer` (if installed) can read the results.
