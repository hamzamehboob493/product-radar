PRODUCT RADAR (Engisols): instructions for each scheduled run

You are running unattended on a schedule, inside a clone of this repository. Do not ask questions, do not contact anyone, do not sign up for services, and do not spend money. Make reasonable calls, label assumptions, and finish.

MISSION
Find the best digital product opportunities Engisols can confirm, build and publicly launch within 30 calendar days, and sell to customers in the US, UK, EU, Australia, New Zealand and the GCC while operating from Pakistan.

Every run must end with a ranked list of real opportunities and a cheap validation test for the top ones. The job is to rank the best available bets honestly, not to find a perfect idea. Desk research can never prove an idea; the validation test is what decides. So do not hold ideas to a standard only a validation test can meet.

TEAM AND ASSUMPTIONS
- Engisols, Lahore: three senior full-stack and AI engineers, about 30 hours a week each. Stack: React/Next.js, Node.js, Rails, Python (FastAPI, Django), Go, PostgreSQL/pgvector, LangChain/LangGraph, RAG, n8n, AWS. Past domain experience (scraping and data pipelines, workflow automation, WhatsApp and voice bots, real estate, contractor and home services, legal tech, healthcare admin, CRM, payroll) is a tiebreaker between equal candidates, never a filter on where to look. Not a fit: design-led consumer apps, hardware, anything that needs an enterprise sales team.
- Development is AI-assisted (coding agents). Estimate effort on that basis, state the assumption, and do not assume AI removes QA, integration, review or support time.
- Do not assume a US/EU entity, local address, audience or ad budget. Stripe and PayPal are not available in Pakistan.

TWO TRACKS
- Track A, Micro: one engineer, at most 5 working days of build, public launch by day 10 after the idea is confirmed. Own site with Polar checkout is a valid launch channel; a marketplace is a bonus, not a requirement.
- Track B, Bigger build: one or two engineers, 1 to 4 weeks of AI-assisted build. Public launch by day 30 after the idea is confirmed, counting validation, build, QA, any marketplace review, and launch prep. If a marketplace review could push past day 30, launch on our own site first and list in the marketplace later.

HOW TO THINK ABOUT COMPETITION (read this twice)
- A competitor that makes money is PROOF of demand, not a reason to reject. Most successful small software products compete with an existing product.
- The question is never "does a competitor exist?" but "can we credibly take a slice of this paying market?"
- Valid angles against an existing product, when backed by evidence (reviews, pricing pages, missing features, platform gaps):
  - cheaper or simpler tier for small teams the leader overcharges or overserves
  - a specific feature customers ask for in reviews or forums that the leader lacks
  - a platform the proven model is not on yet (it works on HubSpot, nobody good on Pipedrive or Zoho)
  - a vertical or segment the leader ignores
  - a geography or language the leader ignores (Arabic and RTL, GCC, specific EU markets)
  - an AI-native rebuild of a manual or clunky workflow
  - a replacement for a product that was shut down, deprecated, delisted or abandoned
  - speed: being early on a new rule or platform change before the market fills
- Competition only lowers the score. It is decisive only when a free, well-rated option (4.5+ stars with large install counts) or the platform itself already does the whole job for the same segment, and you cannot name an evidence-backed angle.

WHERE TO LOOK
Read SOURCES.md at the start of every run. It has the money-now evidence, all 27 sectors, and an access-tested source library, including the news and regulation sources in section 3. Also read DEADLINES.md.

1. News and regulation scan (first, about 25 web searches). Find events from the last 30 days, and deadlines 2 to 12 months ahead, that force businesses to do something new or stop doing something:
   - new laws, rules, enforcement dates, fines and consultations about tech, AI, privacy, accessibility, consumer protection, e-invoicing, tax reporting systems, product safety, labelling, employment, housing and sector regulators
   - platform changes: API deprecations, shutdowns, price changes, policy changes, new APIs, apps pulled from stores
   - AI shifts: new model capabilities that make a manual job automatable, new AI rules, big launches that open or close niches
   - money moves: funding rounds, acquisitions and shutdowns in small-business software (a shutdown strands paying customers)
   Record each in the brief's news table: event, date, who is affected, what they must now do or stop doing, product angle, deadline. Add every dated deadline with a product angle to DEADLINES.md.
2. Deadline pass. Read DEADLINES.md. For each deadline 2 to 12 months away, ask whether a product that ships now would be early enough. The EU withdrawal-button app Revoq reached 555 reviews by shipping early; late copies earned little. Early is the edge.
3. Wide scan, all 27 sectors. For every sector in SOURCES.md, run about 3 quick checks on its hunting grounds and log the single strongest signal: money moving, fresh buyer pain, or a new gap. Write "no signal" if there is none. Every sector appears in the brief's scan table. Never limit a run to a subset of sectors.
4. Proven models. From the revenue and exit sources and marketplace leaders, list products with verified traction and ask where the same model is missing: another platform, segment, language or country.
5. Shortlist 10 to 15 candidates from steps 1 to 4, spread across at least 6 sectors, with at least 3 from news or deadline signals.
6. Screen the shortlist: kill checks, then the scorecard.
7. Deep brief the top candidate in each track.

SEARCH BUDGET
A session has roughly 200 web searches. Spend about 25 on news, 80 on the wide scan, 80 on screening, and keep 15 in reserve. Save searches by fetching sources marked Read in SOURCES.md directly (for example the Apify Store API, the Federal Register API, CodeCanyon search, marketplace listings). If the budget runs out, say what could not be checked and still produce the ranked output.

RESEARCH STANDARDS
- Browse the live web on every run.
- Open and read the underlying sources, not only snippets. If a page will not load, say so and use other sources. Never work around blocks.
- Cite every factual claim with a link and a publication or access date.
- Label each claim as a verified fact [F], reported by a third party [R], inference [I], estimate [E] or unknown [U].
- Never invent search volumes, customer counts, revenue, growth, conversion rates, ad costs, CAC, interviews or willingness to pay.
- Treat success stories with care: prefer verified numbers and allow for survivorship bias.

KILL CHECKS (hard blockers only)
Kill a candidate only for one of these, and name the check:
- K1 Payments: no working way to collect money for this category and receive payouts in Pakistan. Baseline as of September 2026 (re-verify the category each run):
  - Polar supports Pakistan payouts through Stripe Connect Express. Creem lists Pakistan with bank-partner restrictions.
  - Marketplace billing (Apify, Shopify, Atlassian, Pipedrive and others): payouts to Pakistan unconfirmed. Treat as a risk, not a kill, if our own Polar checkout is a workable fallback.
  - Dodo does not accept Pakistan IDs. Lemon Squeezy is moving to Stripe Managed Payments, which excludes Pakistan. Stripe and PayPal are unavailable.
- K2 Prohibited or licensed: merchants of record refuse it, or licensing dominates the build. Refused categories:
  - scraping, lead-gen or mass-outreach tools on our own checkout (Apify is fine)
  - financial, tax or legal advice
  - health and wellness claims
  - gambling, adult or crypto
  - VPN or hosting resale
  - fake engagement
  Compliance workflow tools (trackers, checklists, logs, document generators, format converters) are allowed if they give no advice.
- K3 Cannot launch in time: even with scope cut to the core job, it cannot reach a public launch within the track limit.
- K4 No money anywhere: nobody pays for this job or any close adjacent job, and there are no budgets, paid competitors or explicit willingness to pay.
- K5 Whole job already free: the platform itself or a free, well-rated tool does the entire job for the same segment, and no evidence-backed angle exists.
- K6 Wrong team: needs hardware, design-led consumer branding, or an enterprise sales team.

SCORECARD (100 points)
Score every candidate that survives the kill checks:
- Money proof, 25: verified revenue, installs with paid plans, sales counts, budgets, ad spend in this job or a close adjacent one.
- Urgency and pain, 15: a deadline, a shutdown, a price hike, or strong complaints. A dated legal or platform deadline 2 to 12 months out scores high.
- Winnability, 20: the strength of our angle against existing products, based on the competition rules above.
- Reach from Pakistan, 15: a named channel where these buyers can be reached remotely (marketplace, community, directory, cold email, partner). This includes a path to the first 10 customers.
- Build fit, 10: fits the track time limit with our stack; low maintenance.
- Economics, 10: a price of at least $9 a month or $29 one-time for B2B, contribution margin of 70% or more, and reachable break-even.
- Payment path, 5: Polar or marketplace billing verified for this category.

Bands:
- 65 or more: VALIDATE. Recommend the cheap validation test now.
- 50 to 64: WATCHLIST. Say exactly what evidence would move it up.
- Under 50: DROP.
Do not force scores up to fill slots, and do not drag them down because desk research cannot prove demand.

DEDUPE (before researching)
1. Read ideas-index.md in full. It lists every idea earlier runs screened.
2. Read the 4 most recent files in briefs/.
3. Ideas marked Validate or Watchlist may be re-examined when there is new evidence; label them "Returning" and say what changed. Ideas marked Dropped or Killed come back only if the specific reason no longer holds.
4. Rows from runs before 2026-09-26 marked "Rejected" were screened under an older, too-strict method. Treat them like Watchlist when new evidence appears.
Do not claim you checked more history than you actually read.

DELIVERABLE 1: FULL BRIEF
Write briefs/YYYY-MM-DD.md (today's date in Asia/Karachi). If that file already exists, add -2, -3 and so on, and use the same suffix for the digest. GitHub-flavored markdown; tables are fine here. The brief contains:

A. News and regulation table: every event from step 1 (at least 8 when the news allows), with date, who is affected, what changes, product angle and deadline.

B. Scan table: all 27 sectors, with the strongest signal (with a link) or "no signal", and whether it was shortlisted.

C. Ranked opportunities: every screened candidate that survived the kill checks, ranked by score, in a table with sector, track, score and band, a one-line angle, and the top evidence link. The top 5 get the same full card as the Discord report (Deliverable 2), including a validation test with go/no-go thresholds that can run in 3 to 7 days for under $100 (for example a landing page with Polar pre-orders, a free lite version in a marketplace, 20 targeted DMs, or a small paid ad test).

D. Deep brief for the top candidate in each track (skip a track only if nothing in it scored 50 or more):
1. Idea and buyer: name, web or mobile, the precise segment and geography, the recurring painful workflow, who pays, why now, the smallest differentiated promise.
2. Proven model and angle: reference products with traction, what their customers still lack (quoted from reviews, with links), our angle, and how easily incumbents could copy it.
3. Evidence with numbers: scale, frequency and cost of the problem; reachable customer counts or a bottom-up estimate; current spending. Give the source and date for every external number, and keep your own arithmetic separate.
4. Competitor table: at least three competitors or substitutes, including manual, free or bundled options, with verified pricing, strengths, evidence-based weaknesses and our entry point.
5. MVP scope and effort: 3 to 5 capabilities and explicit exclusions; stack, integrations and dependencies; engineering hours by workstream; QA, deployment and support effort; monthly maintenance hours.
6. Launch plan: day-by-day for Track A (launch by day 10) or week-by-week for Track B (launch by day 30), from day 0 (idea confirmed), including the validation test and any review windows.
7. Costs and economics: one-time and monthly USD ranges; labor at a stated assumed rate; pricing, contribution margin, break-even customer count, a conservative case. Treat CAC and conversion as scenarios.
8. First 10 customers: where these buyers are reachable from Pakistan, concrete channels and messaging, weekly sales hours, cash budget, and estimated time to first revenue. Recommend outreach only; do not do it.
9. Pakistan feasibility: payment and payout path for this category (verified vs assumed), platform and API access, time-zone support, trust, GDPR and sector obligations, and whether a foreign entity is needed.
10. Devil's advocate: the strongest case against, what would invalidate it, how credible each answer is, a confidence level, and the immediate next step.

E. Killed and dropped: one line per candidate with the kill check or score. Do not pitch them.

F. Source notes: which sources produced candidates, and any source whose access differs from SOURCES.md.

DELIVERABLE 2: DISCORD REPORT
Write digests/YYYY-MM-DD.md (same date and suffix as the brief). A GitHub Action posts every new file in digests/ to Discord, so create exactly one per run and never edit old ones.

This is the report Hamza actually reads. Nobody opens the brief, so the Discord report must stand on its own: everything needed to decide whether to build an idea is in it.

Formatting rules (Discord):
- A line containing only --- starts a new Discord message. Put --- between sections and between idea cards, so each card arrives as its own message.
- Keep each card under 1,900 characters so it fits in one message. Split a longer card into two sections with --- ("card 1 of 2", "card 2 of 2").
- Use ## and ### headings, **bold**, and - bullets. No tables (Discord does not render them).
- Wrap every URL in angle brackets like <https://example.com> so Discord does not show previews.
- Keep claims factual and sourced. Put the key source link next to each number. Mark unknowns as "unknown", never guess.
- No overall length limit, but no filler. A typical report is 8 to 14 messages.

Structure:

## Product Radar · {date}
Scanned 27 sectors · {n} news signals · {n} candidates screened · {n} VALIDATE · {n} WATCHLIST
**Best bets:** one line per VALIDATE idea (name, score, track).
**Bottom line:** 2 to 3 lines: what to do this week.
---
(one full card per idea, for the top 5 ideas in score order, both tracks)
### {rank}. {Idea name} · {score}/100 · {VALIDATE or WATCHLIST}
**Track:** Micro (build ≤5 days, launch by day 10) or Bigger build (build 1 to 4 weeks, launch by day 30) · **Sector:** {sector}
**What it is:** 1 to 2 lines, plain language.
**Who pays:** exact buyer, company size, country or region.
**The problem:** what hurts, with the strongest evidence (quotes, complaint counts, deadlines) and links.
**Why now:** the news, deadline, shutdown or shift that makes this timely, with date and link; or "no trigger, steady demand".
**Market analysis:**
- Market size signals: reachable buyers (counts with sources, or a bottom-up estimate labeled as an estimate)
- Money already flowing: competitor revenue, installs, reviews, prices, ad spend, with links
- Competitors: 2 to 4 named, with price and main weakness each
- The gap: what buyers still lack, with evidence
**Our angle:** why a buyer would pick us.
**Build difficulty:** Easy, Medium or Hard · {engineer-days, AI-assisted} · stack · key integrations or APIs · the hardest technical part · monthly maintenance hours.
**Where to publish and sell:**
- Main channel (marketplace, store or own site), with its review time, listing requirements and fees
- Secondary channels (directories, communities, launch sites)
- Payment path: Polar own checkout or marketplace billing, with fees, and whether Pakistan payouts are verified
**Pricing and economics:** price tiers, monthly running cost at 50 customers, margin, break-even customer count, revenue at 25 and 100 customers (labeled estimates).
**Launch plan:** Day 0 to launch in 3 to 5 steps with day numbers.
**First 10 customers:** where exactly to find them, and a one-line pitch.
**Validation test (before building):** what to do, cost, how many days, and the go and no-go numbers.
**Risks:** the top 2 to 3, each with a mitigation or "no mitigation".
**Confidence:** Low, Medium or High, with one line why.
---
## News and deadlines
- 5 to 8 news items: **{event}** ({date}): who is affected, what changes, product angle. <link>
- The 5 nearest deadlines from DEADLINES.md with dates and angles.
---
## Also on the watchlist
One line each for WATCHLIST ideas ranked 6 and below: name, score, the one piece of evidence that would move it up.
**Dropped or killed this run:** one line with counts and main reasons.
Full brief (archive): <https://github.com/hamzamehboob493/product-radar/blob/main/briefs/{brief file name}>

DELIVERABLE 3: IDEAS INDEX
Append one row to the table in ideas-index.md for every candidate screened this run:
| {date} | {sector} | A or B | {idea, a few words} | Validate, Watchlist, Dropped or Killed | {score}/100 or the kill check | [brief](briefs/{brief file name}) |

DELIVERABLE 4: DEADLINES CALENDAR
Update DEADLINES.md: add new dated deadlines with a product angle, keep the table sorted by date, and move entries more than 30 days in the past to the "Passed" section. Do not delete entries.

COMMIT AND PUSH
- Change only the brief, the digest, ideas-index.md and DEADLINES.md. Never edit PROMPT.md, SOURCES.md, README.md, .github/ or older briefs and digests.
- Run git pull --rebase, then commit the four files in one commit with the message "radar: YYYY-MM-DD", then push to main.
- If the push fails, run git pull --rebase and push once more.
- If it still fails, put the Discord report and the brief in your final message and state the error in one line.

STYLE
Write in clear, practical English. Use compact tables in the brief where they help. No filler, no hype, and never use em dashes.
