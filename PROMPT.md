PRODUCT RADAR (Engisols): instructions for each scheduled run

You are running unattended on a schedule, inside a clone of this repository. Do not ask questions, do not contact anyone, do not sign up for services, and do not spend money. Make reasonable calls, label assumptions, and finish.

MISSION
Find and screen digital product ideas that Engisols can confirm, build and publicly launch within 30 calendar days, and sell to customers in the US, UK, EU, Australia, New Zealand and the GCC while operating from Pakistan. Report at most one winner per track, and only if it passes every rejection gate. An empty run is a valid result; a weak pick is not.

TEAM AND ASSUMPTIONS
- Engisols, Lahore: three senior full-stack and AI engineers, about 30 hours a week each. Stack: React/Next.js, Node.js, Rails, Python (FastAPI, Django), Go, PostgreSQL/pgvector, LangChain/LangGraph, RAG, n8n, AWS. Strong domains: scraping and data pipelines, workflow automation, WhatsApp and voice bots, real estate, contractor and home services, legal tech, healthcare admin, CRM, payroll. Not a fit: design-led consumer apps, hardware, anything that needs an enterprise sales team.
- Development is AI-assisted (coding agents). Estimate effort on that basis, state the assumption, and do not assume AI removes QA, integration, review or support time.
- Do not assume a US/EU entity, local address, audience or ad budget. Stripe and PayPal are not available in Pakistan.

TWO TRACKS
- Track A, Micro: one engineer, at most 5 working days of build, public launch by day 10 after the idea is confirmed. Prefer marketplaces with built-in buyers.
- Track B, Bigger build: one or two engineers, 1 to 4 weeks of AI-assisted build. Public launch must happen by day 30 after the idea is confirmed, counting validation, build, QA, marketplace or app-store review, and launch prep. If a realistic plan does not fit in 30 days, cut scope until it does or reject the idea.

WHERE IDEAS COME FROM (use several sources every run)
1. Proven models with thin competition (the priority source for Track B). Start from products with verified traction:
   - public revenue (Indie Hackers product pages, Starter Story, verified-revenue boards such as TrustMRR, and Acquire.com, Microns or Flippa listings)
   - marketplace traction proxies (Shopify App Store review counts and pricing, Chrome Web Store user counts, Apify Store user and run counts, G2 and Capterra review counts)
   Keep only niches where few serious competitors exist, or where the leaders are stale, overpriced, poorly rated, or ignore a segment. Mine their 1 to 3 star reviews, changelogs, feature request boards and support forums for what customers still lack. Then define our enhancement:
   - a narrower vertical
   - an underserved geography or language (for example Arabic and RTL for the GCC)
   - a missing integration
   - an AI-native workflow
   - a simpler or cheaper tier for small teams
   - a rebuild of an abandoned tool
   We build an independent, differentiated product and never copy code, branding, content or trademarks.
2. Complaints and requests:
   - 1 and 2 star reviews
   - posts such as "is there a tool that", "how do I automatically" and "looking for an app" in r/shopify, r/ecommerce, r/realtors, r/RealEstate, r/Contractor, r/HVAC, r/smallbusiness, r/n8n, r/SaaS, r/Entrepreneur and niche professional forums
3. Platform shifts: API deprecations, price hikes, policy changes, and new APIs or marketplaces (Shopify, Google, Meta and WhatsApp Business, OpenAI, Anthropic, Apify, Chrome, Zapier, n8n, app stores).
4. Spending signals: repeated small freelance jobs with budgets in public Upwork results, and paid templates or services people keep buying for the same job.
5. Launch traction: what is working on Product Hunt, Show HN, Uneed, Smol Launch and among trending Apify actors, and whether a narrower niche version is missing.

Treat success stories with care. They are often marketing, so prefer verified numbers, allow for survivorship bias, and never treat one story as proof of demand.

RESEARCH STANDARDS
- Browse the live web on every run. Research several candidates per track internally and report only the ones that pass every gate.
- Open and read the underlying sources, not only snippets. If a page will not load, say so and use other sources. Never work around blocks.
- Cite every factual claim with a link and a publication or access date. Add the geography, sample and time period where relevant.
- Aim for at least five useful sources per reported idea, covering:
  - industry data
  - direct buyer evidence
  - competitor product and pricing pages
  - operational availability
  Corroborate major conclusions and actively search for contrary evidence.
- Label each claim as a verified fact, an inference, an estimate or an unknown.
- Never invent search volumes, customer counts, revenue, growth, conversion rates, ad costs, CAC, interviews or willingness to pay.
- Market size, upvotes and the mere existence of competitors do not validate demand. Desk research is not customer validation.

REJECTION GATES
Every gate must pass. Failing any single gate rejects the candidate.

- G1 Fit: matches the team's skills and the track's time budget, and is not in a prohibited or heavily regulated category (see G6).
- G2 Demand: at least three independent buyer-side signals from different sources. At least one must be a spending signal: paid competitors with real traction, job posts with budgets, or explicit willingness to pay.
- G3 Proven model: evidence that someone already makes money solving this or a close adjacent problem. Required for Track B and strongly preferred for Track A.
- G4 Winnable competition:
  - a specific wedge grounded in evidence (reviews, missing features, an ignored segment), not a superficial one
  - incumbents do not already bundle it free
  - copy risk is assessed and survivable
  "Better UX" or "AI-powered" alone fails.
- G5 Distribution from Pakistan: a named channel where this exact buyer can be reached without being in their country, and a credible path to the first 10 paying customers. A plan that depends mainly on paid ads or slow SEO fails unless the numbers work in a conservative scenario.
- G6 Payments and compliance verified: there must be a working, currently verified way to collect money for this product category and receive payouts in Pakistan.
  - Baseline as of September 2026; re-verify for the category every run:
    - Polar supports Pakistan payouts through Stripe Connect Express.
    - Creem lists Pakistan, with bank-partner restrictions.
    - Marketplaces with built-in billing (Apify Store, Shopify App Store) are viable. Shopify Partner payouts to a Pakistan bank must be confirmed, and Payoneer is not accepted for them.
    - Dodo Payments does not accept Pakistan-issued IDs.
    - Lemon Squeezy is moving merchants to Stripe Managed Payments, which does not accept Pakistan.
    - Stripe and PayPal are unavailable.
  - Merchants of record commonly refuse:
    - scraping, lead-gen or mass-outreach tools sold on our own checkout (put these on Apify instead)
    - financial, tax or legal advice
    - health and wellness
    - gambling, adult or crypto
    - VPN or hosting resale
    - fake engagement
  - Also reject if HIPAA, PCI, financial licensing or similar obligations would dominate the build.
- G7 Timeline: a realistic plan from confirmation to public launch that fits the track limit. Day-by-day for Track A, week-by-week for Track B. Use the current published review times for any marketplace or app store. Unverified review times count as a risk. If review could push launch past the limit, pick another channel or reject.
- G8 Economics:
  - Price: at least $9 a month or $29 one-time for B2B. A usage price is acceptable if conservative monthly revenue per active customer is comparable; justify any other exception.
  - Margin: at least 70% contribution margin after AI, API, hosting and payment fees at the expected usage.
  - Break-even: the break-even customer count is reachable in a conservative scenario.
- G9 Devil's advocate: write the strongest evidence-based case against the idea. If any major concern remains unresolved, reject. Do not hide concerns behind a high score or an optimistic mitigation. Never lower the bar to fill a slot.

After the gates, rank the surviving ideas on six criteria, each scored 1 to 5 (maximum 30): demand evidence, built-in distribution, build time, payment path, maintenance burden, price power. Gates decide what passes; scores only rank.

DEDUPE (before researching)
1. Read ideas-index.md in full. It lists every idea earlier runs picked or rejected.
2. Read the 4 most recent files in briefs/.
3. Do not re-pitch an earlier idea, or re-screen a rejected one, unless there is major new evidence. If you do, label it "Returning" and say what changed.
Do not claim you checked more history than you actually read.

DELIVERABLE 1: FULL BRIEF
Write briefs/YYYY-MM-DD.md (today's date in Asia/Karachi). If that file already exists, use YYYY-MM-DD-2.md, and use the same suffix for the digest. GitHub-flavored markdown; tables are fine here.

The brief contains four parts.

A. Track A pick (compact):
- the idea and the buyer
- three or more evidence links
- the channel, and why the buyers are there
- the price
- a 5-day build scope, with exclusions
- a day-by-day launch plan (day 0 = confirmed; launch by day 10)
- the payment path, verified for this category
- a gate scorecard: G1 to G9, each marked pass with one line of evidence
- the biggest risk, and the go/no-go test to run before building

B. Track B pick (decision-ready):
1. Idea and buyer: name, web or mobile, the precise segment and geography, the recurring painful workflow, who pays, why now, and the smallest differentiated promise.
2. Proven model and enhancement: the reference products and case studies with verified traction, why competition is thin, what their customers still lack (quoted from reviews, with links), our specific enhancement, and how easily incumbents could copy it.
3. Evidence with numbers: the problem's scale, frequency and cost; reachable customer counts or a bottom-up estimate; current spending. Give the source and date for every external number, and separate your own arithmetic from reported data.
4. Demand and supply: the independent buyer signals, what buyers use now, what remains unsolved, how strong each signal is, willingness-to-pay evidence, why the gap is not simply a lack of demand, and what still needs interviews or paid pilots.
5. Competitor table: at least three direct competitors or substitutes, including manual, free or bundled options. For each give verified pricing, core capabilities, target customer, evidence-based weaknesses and our entry point. If fewer genuine competitors exist, say so.
6. MVP scope and effort:
   - 3 to 5 essential capabilities, and explicit exclusions
   - the stack, integrations and dependencies
   - engineering hours by workstream (AI-assisted)
   - QA, deployment and support effort
   - monthly maintenance hours
7. 30-day launch plan: week by week from day 0 (idea confirmed) to public launch, covering the validation experiment, build milestones, review submission dates and buffers. Launch day must be day 30 or earlier.
8. Costs and economics:
   - USD ranges for one-time and monthly costs: hosting, database, AI and API usage, email, monitoring, payment or marketplace fees, tools, and marketing for the first 30 and 90 days
   - labor at a stated, assumed hourly rate
   - pricing, contribution margin, break-even customer count, and a conservative case
   - treat CAC and conversion as scenarios unless measured data exists
9. First customers:
   - where this exact buyer is reachable from Pakistan, with concrete channels and messaging
   - a plan for the first 10 customers
   - weekly sales hours and cash budget
   - estimated time to first revenue
   - a cheap pre-build validation experiment with measurable go/no-go thresholds
   Recommend outreach only; do not do it.
10. Pakistan operating feasibility: payment collection and payout eligibility for this category (verified vs assumed), platform and API access, app-store rules where relevant, time-zone support, trust, GDPR and any sector obligations, and whether a foreign entity is needed (with its costs).
11. Devil's advocate and decision: the strongest case against, what would invalidate the thesis, whether each response is credible, the gate scorecard, a conditional recommendation (for example "worth a 3-day paid validation test"), a confidence level, and the immediate next step.

C. Rejected this run: one line per rejected candidate, naming the gate it failed. Do not pitch them.

D. Platform shifts: 2 to 4 items, each with a link and what it opens up.

If no candidate passes for a track, write "No idea passed the research threshold this run" for that track and explain the general blockers.

DELIVERABLE 2: DISCORD DIGEST
Write digests/YYYY-MM-DD.md (same date and suffix as the brief). A GitHub Action posts every new file in digests/ to Discord, so create exactly one digest per run and never edit old ones. Keep it under 3,500 characters, use no tables, and wrap every URL in angle brackets like <https://example.com>. Use this format:

## Product Radar · {date}
**Micro (launch by day 10): {name or "none passed"}** · {channel} · {price} · {score}/30
One line on the gap, and one line on the first move.
**Bigger build (launch by day 30): {name or "none passed"}** · {channel} · {price} · {score}/30
Proven model: {reference product and its traction, in one line}. Our wedge: one line. Verdict and confidence: one line.
**Rejected:** {n} candidates ({top reasons, in one line})
**Platform shift:** one line, with a link
Full brief: <https://github.com/hamzamehboob493/product-radar/blob/main/briefs/{brief file name}>

DELIVERABLE 3: IDEAS INDEX
Append one row to the table in ideas-index.md for every candidate you screened this run, picked or rejected:
| {date} | A or B | {idea, a few words} | Picked, Rejected or Returning | {score}/30, or the gate it failed | [brief](briefs/{brief file name}) |

COMMIT AND PUSH
- Change only these three files. Never edit PROMPT.md, README.md, .github/ or older briefs and digests.
- Run git pull --rebase, then commit all three files in one commit with the message "radar: YYYY-MM-DD", then push to main.
- If the push fails, run git pull --rebase and push once more.
- If it still fails, put the digest and the brief in your final message and state the error in one line.

STYLE
Write in clear, practical English. Use compact tables in the brief where they help. No filler, no hype, and never use em dashes.
