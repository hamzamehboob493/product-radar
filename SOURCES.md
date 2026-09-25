# Research sources

The radar's source library: where money is flowing now, the 27 sectors every run scans, and which sources a scheduled run can actually read.

Last checked: 2026-09-25 (about 75 sources tested). Runs report sources that fail in their brief.

**Access key**
- **Read:** loads with the web-fetch tool and shows usable data.
- **Partial:** loads, but shows only part of the data (noted in the row).
- **Search:** blocks bots, needs login, or renders with JavaScript. Use web search with `site:` queries and read the snippets.
- **Connector:** use the named connector's tool.
- **Untested:** listed for completeness; try it and report the result in the brief.

## 1. Where money is flowing now (evidence as of Sep 2026)

| Signal | What it shows | Source |
|---|---|---|
| Verified startup revenue | Top categories by revenue are E-commerce, Content Creation and Entertainment, and Content Creation had the fastest 30-day growth. The page was updated Sep 23, 2026. Its dollar totals look inconsistent, so use only the category ranking. | [TrustMRR stats](https://trustmrr.com/stats) |
| Consumer AI | Agentic AI is a new category (Genspark reports a $100M revenue run rate). AI coding is booming (Claude Code at a $1B run rate; Replit, Lovable). Video generation is rising. AI features inside existing tools are converting (Notion's paid AI attach rate went from 20% to over 50%). Published Mar 9, 2026. | [a16z Top 100 Gen AI Consumer Apps](https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march) |
| App store revenue | 2025 leaders: TikTok $3.35B, Google One $2.64B, ChatGPT $2.36B, YouTube $2.10B. Streaming, AI, cloud storage, dating and games dominate. Updated Jan 27, 2026. | [Business of Apps](https://www.businessofapps.com/data/top-grossing-apps/) |
| Monthly app revenue | February 2026: ChatGPT had 51M downloads and $194M net revenue; TikTok had $286M net revenue. | [Appfigures](https://appfigures.com/resources/insights/most-downloaded-highest-earning-apps-february-2026) |
| Creator and community economy | Whop claims "$4.6B+ paid to businesses on Whop". On Skool, paid AI communities charge around $9/month (for example AI Video Bootcamp, 28.3k members). The top-ranked Patreon creator is a podcast. | [Whop](https://whop.com/discover/), [Skool](https://www.skool.com/discovery), [Graphtreon](https://graphtreon.com/top-patreon-creators) |
| Marketplace sellers | "On TikTok Shop, 1% of Sellers Drive 60% of GMV". Amazon is opening Seller Central to rival marketplaces. Amazon FBA and FBM businesses are actively bought and sold on Empire Flippers. | [Marketplace Pulse](https://www.marketplacepulse.com/articles), [Empire Flippers](https://empireflippers.com/marketplace/) |
| Freelance spend | Visible AI gigs include AI UGC video ads for ecommerce and AI bot setups. | [Fiverr AI coding](https://www.fiverr.com/categories/programming-tech/ai-coding) |
| Platform shifts | Shopify script tags are deprecated and stop running Mar 1, 2027. HubSpot sunsets the Pipelines API v1 on Dec 4, 2026. | [Shopify changelog](https://shopify.dev/changelog), [HubSpot changelog](https://developers.hubspot.com/changelog) |

Takeaway: money is concentrating in e-commerce sellers, content creators and communities, entertainment, AI inside tools people already use, AI agents, and developer tools. Platform deprecations keep creating forced-migration demand.

## 2. Sectors (all 27 are scanned every run)

Every run scans all 27 sectors, then goes deep on the strongest candidates from any sector. Each sector lists who pays, where to hunt, and any cautions. Subreddits are Search access (use `site:reddit.com`).

1. **E-commerce and marketplace sellers** (Shopify, Amazon, TikTok Shop, Etsy, WooCommerce)
   - Who pays: store owners, brands, agencies.
   - Where to hunt: Shopify App Store, WooCommerce marketplace, Shopify changelog, Marketplace Pulse, Amazon Movers & Shakers, Empire Flippers (what sellers run), Meta Ad Library; r/shopify, r/ecommerce, r/FulfillmentByAmazon, r/EtsySellers, r/printondemand, r/dropship.
2. **Marketing and advertising** (SMB marketers, agencies, ad creative, SEO and AI-search visibility, social, email)
   - Where to hunt: G2 and Capterra marketing categories, HubSpot marketplace, Meta Ad Library, Fiverr, Upwork; r/PPC, r/SEO, r/marketing, r/socialmedia, r/agency, r/Emailmarketing, r/copywriting.
3. **Sales and revenue ops** (CRM add-ons, pipeline hygiene, call notes, quoting, renewals)
   - Where to hunt: HubSpot marketplace and changelog, Salesforce AppExchange, G2 sales categories, Upwork; r/sales, r/salesforce, r/hubspot.
   - Caution: merchants of record refuse lead scraping and mass outreach tools.
4. **Content creation and the creator economy** (YouTube, TikTok, podcasts, newsletters, UGC, clipping)
   - Where to hunt: TrustMRR Content Creation, a16z list, Fiverr, Graphtreon, Whop; r/NewTubers, r/youtubers, r/podcasting, r/Newsletters, r/editors.
5. **Entertainment, media and communities** (Discord servers, Skool and Whop communities, fandoms, streaming tools)
   - Where to hunt: Skool, Whop, Graphtreon, SteamDB, top.gg, TrustMRR Entertainment; r/Twitch, r/discordapp.
   - Caution: games, virtual goods and gambling are refused. Sell tools to creators and community owners.
6. **Developer tools and AI infrastructure** (coding agents, MCP servers, testing, observability, devops)
   - Where to hunt: GitHub trending, Show HN, Glama, Smithery, Hugging Face Spaces, Raycast Store, JetBrains and VS Code marketplaces; r/webdev, r/devops, r/LocalLLaMA.
7. **AI agents and automation for small businesses** (voice receptionists, WhatsApp agents, inbox and back-office agents)
   - Where to hunt: a16z agentic category, Upwork automation jobs, Fiverr, Zapier, n8n, Apify; r/AI_Agents, r/n8n, r/automation, r/smallbusiness.
8. **Product marketing and SaaS growth** (onboarding, analytics, pricing pages, feedback, changelogs, churn)
   - Where to hunt: G2, Latka, TrustMRR SaaS, Indie Hackers, Product Hunt, SaaSHub, AlternativeTo; r/SaaS, r/ProductManagement, r/startups.
9. **Productivity, templates and browser tools** (Notion, Google Workspace, Sheets, Chrome extensions, launchers)
   - Where to hunt: chrome-stats, Google Workspace Marketplace, Raycast Store, Notion templates, Framer marketplace, CodeCanyon, Zapier, ChatGPT apps directory; r/Notion, r/googlesheets, r/Airtable, r/ChatGPTPro.
10. **Design and creative professionals** (designers, photographers, video editors, musicians)
    - Where to hunt: Figma Community, Framer marketplace, ThemeForest and CodeCanyon, Fiverr; r/FigmaDesign, r/UXDesign, r/photography, r/editors, r/WeAreTheMusicMakers.
11. **Home services and construction** (HVAC, plumbing, electrical, roofing, cleaning, landscaping)
    - Where to hunt: Capterra field-service categories, Trustpilot, Meta Ad Library; r/Contractor, r/HVAC, r/Plumbing, r/electricians. ContractorTalk blocks the fetch tool.
12. **Real estate and property management** (agents, investors, landlords, short-term rental hosts)
    - Where to hunt: BiggerPockets forums, Capterra property management, HubSpot marketplace; r/RealEstate, r/realtors, r/PropertyManagement, r/airbnb_hosts.
13. **Legal, accounting and professional services** (practice admin only)
    - Where to hunt: Capterra legal and accounting categories, G2; r/Lawyertalk, r/Accounting, r/Bookkeeping.
    - Caution: no legal or tax advice features.
14. **Clinic and practice admin** (scheduling, intake, reminders and reviews for clinics, dentists, therapists)
    - Where to hunt: Capterra medical practice categories, Trustpilot; r/dentistry, r/physicaltherapy.
    - Caution: health products are refused by some merchants of record, and HIPAA applies. Keep to admin workflows with minimal patient data.
15. **Hospitality, restaurants and events** (restaurant operators, venues, event organisers)
    - Where to hunt: Capterra restaurant and event categories, Trustpilot; r/restaurateur, r/KitchenConfidential.
    - Caution: ticketing and booking resale is refused. Sell operator tools.
16. **Beauty, fitness and personal services** (salons, gyms, studios, coaches)
    - Where to hunt: Capterra salon and gym categories, Skool (coaches); r/HairStylist, r/personaltraining.
    - Caution: no health claims.
17. **Education and e-learning** (course creators, tutors, students, training teams)
    - Where to hunt: Skool, Whop, Starter Story, Google Workspace Marketplace education apps; r/Teachers, r/Professors.
18. **HR, recruiting and freelancing** (hiring pipelines, contractor management, freelancer tools)
    - Where to hunt: G2 HR categories, Upwork, Fiverr, hnhiring; r/recruiting, r/humanresources, r/freelance.
19. **Finance operations for small businesses** (invoicing, receivables, expense capture, reconciliation helpers)
    - Where to hunt: G2 and Capterra accounting categories, QuickBooks and Xero app marketplaces (Untested); r/Bookkeeping, r/smallbusiness.
    - Caution: no financial or tax advice, no holding or moving money, no tax calculators sold on a merchant-of-record checkout.
20. **Logistics, supply chain and manufacturing** (small shippers, 3PLs, workshops)
    - Where to hunt: Capterra inventory and warehouse categories, Marketplace Pulse; r/logistics, r/supplychain, r/manufacturing.
21. **Compliance and regulation-driven products** (EU AI Act, accessibility, product safety, privacy, email authentication)
    - Where to hunt: EU AI Act timeline, platform changelogs, regulator news via search.
    - Caution: no legal advice. Sell checkers, trackers and workflows.
22. **Security and IT for small businesses and MSPs**
    - Where to hunt: G2 security categories, Exploding Topics, Glama; r/msp, r/sysadmin.
23. **Nonprofits, associations and membership organisations**
    - Where to hunt: Capterra nonprofit and membership categories; r/nonprofit.
    - Caution: donation and fundraising products are refused. Sell admin tools.
24. **Automotive** (dealers, repair shops, detailers)
    - Where to hunt: Capterra auto repair and dealer categories, Trustpilot, Meta Ad Library.
25. **Consumer hobby niches with paying users** (pets, weddings, gardening, fitness hobbyists)
    - Where to hunt: Exploding Topics, Apple App Store charts, Etsy (Search).
    - Caution: consumer acquisition is expensive. The idea needs a cheap channel to pass G5.
26. **GCC and Arabic-first** (any sector where Arabic, RTL, cash on delivery or local portals are unserved)
    - Where to hunt: the other sectors' sources filtered to SA and AE, Meta Ad Library with SA and AE countries.
    - Caution: check the payments gate early.
27. **Data products and APIs** (Apify Actors, datasets, enrichment endpoints)
    - Where to hunt: Apify Store, Glama, Smithery.
    - Caution: sell scrapers only through Apify, never on our own checkout.

## 3. Source library by signal type

### Proven revenue and exits ("is anyone making money here?")
| Source | Access | Use it for |
|---|---|---|
| [TrustMRR](https://trustmrr.com/category) | Read | Stripe-verified revenue in 31 categories; open a category and sort by revenue. |
| [Indie Hackers products](https://www.indiehackers.com/products) | Read | Self-reported monthly revenue per product; treat as unverified. |
| [Starter Story ideas](https://www.starterstory.com/ideas) | Read | Case studies and ideas with monthly revenue figures; verify before relying on them. |
| [Latka](https://getlatka.com/) | Read | SaaS companies with CEO-stated revenue, growth and team size. |
| [Microns](https://www.microns.io/) | Read | Small startups for sale with annual revenue and asking price. |
| [Empire Flippers](https://empireflippers.com/marketplace/) | Read | Businesses for sale with price, net profit, niche and model (Amazon FBA and FBM, content, SaaS). |
| [SideProjectors](https://www.sideprojectors.com/) | Partial | Side projects for sale; revenue is often missing. |
| [Acquire.com](https://acquire.com/) | Search | Listings need login. |
| [Flippa](https://flippa.com/) | Partial | Listing figures render with JavaScript. |
| [Sacra](https://sacra.com/) | Search | Revenue estimates for private companies; mostly paywalled, but company pages show up in search. |

### Marketplace traction ("are buyers already paying inside a store?")
| Source | Access | Use it for |
|---|---|---|
| [Shopify App Store](https://apps.shopify.com/) | Read | Review counts, ratings and pricing; bad reviews of big apps show the gaps. |
| [WooCommerce marketplace](https://woocommerce.com/products/) | Read | Extension prices, ratings and review counts. |
| [Apify Store](https://apify.com/store) | Read | Uses, ratings and pricing per Actor. |
| [WordPress plugins](https://wordpress.org/plugins/browse/popular/) | Read | Active installs and ratings. |
| [CodeCanyon](https://codecanyon.net/popular_item/by_category?category=php-scripts) and ThemeForest | Read | Prices, ratings and sales counts for scripts, plugins and templates. |
| [Framer marketplace](https://www.framer.com/marketplace/templates/) | Read | Template prices; shows what site buyers pay for. |
| [Notion templates](https://www.notion.com/templates) | Partial | Creators and prices; no sales data. |
| [Google Workspace Marketplace](https://workspace.google.com/marketplace/category/popular-apps) | Read | Users (for example Colaboratory 95M+) and ratings per add-on. |
| [Atlassian Marketplace](https://marketplace.atlassian.com/search?sort=top-selling) | Read | Top-selling Jira and Confluence apps with installs and ratings. |
| [HubSpot Marketplace](https://ecosystem.hubspot.com/marketplace/apps) | Read | Install counts per app. |
| [Zapier apps](https://zapier.com/apps) | Read | Popular apps; integrations that don't exist yet. |
| [Raycast Store](https://www.raycast.com/store) | Read | Extension install counts. |
| [top.gg](https://top.gg/) | Read | Discord bots with vote counts. |
| [Glama MCP servers](https://glama.ai/mcp/servers) | Read | MCP servers with weekly npm downloads and GitHub stars. |
| [Smithery](https://smithery.ai/) | Read | MCP servers with use counts. |
| [Hugging Face Spaces](https://huggingface.co/spaces?sort=trending) | Read | Trending AI demos worth turning into products. |
| [chrome-stats](https://chrome-stats.com/) | Read | Chrome extension users, ratings and growth. The Chrome Web Store itself blocks the fetch tool. |
| [ChatGPT apps directory](https://chatgpt.com/apps) | Partial | Categories and names only. |
| [n8n workflows](https://n8n.io/workflows/) | Partial | Creators only. |
| Salesforce AppExchange, Slack Marketplace, Figma Community, JetBrains Marketplace, VS Code Marketplace, PulseMCP | Search | JavaScript pages, robots.txt blocks, or URL changes. |

### Consumer and app revenue
| Source | Access | Use it for |
|---|---|---|
| [a16z Top 100 Gen AI Consumer Apps](https://www.a16z.news/p/top-100-gen-ai-consumer-apps-march) | Read | Which AI categories are growing; a new edition comes out roughly every six months. |
| [Appfigures insights](https://appfigures.com/resources/insights/most-downloaded-highest-earning-apps-february-2026) | Read | Monthly top-earning apps with revenue estimates. |
| [Business of Apps](https://www.businessofapps.com/data/top-grossing-apps/) | Read | Yearly top-grossing apps and categories. |
| [Apple App Store charts](https://apps.apple.com/us/charts/iphone) | Partial | App names in the top charts; no revenue. |
| [Similarweb top websites](https://www.similarweb.com/top-websites/) | Partial | Traffic ranks, no visit numbers. |
| AppMagic top charts | Search | Rendered with JavaScript. |

### Ad spend ("is someone paying to reach these buyers?")
| Source | Access | Use it for |
|---|---|---|
| Meta Ad Library | Connector | Use the Meta Ads connector's `ads_library_search` with search terms and a country. `estimated_total_count` of active ads is a rough spend signal (for example "shopify app" in the US returned about 2,295 active ads). Advertisers running the same offer for weeks suggest it pays back. |
| Google Ads Transparency Center | Search | The page is a JavaScript shell. |
| TikTok Creative Center | Search | The page is a JavaScript shell. |

### Demand and pain ("who is asking, and what do they hate?")
| Source | Access | Use it for |
|---|---|---|
| Reddit | Search | Blocked for the fetch tool. Search `site:reddit.com "is there a tool" <niche>` and `site:reddit.com <competitor> alternative`. |
| [Hacker News](https://news.ycombinator.com/show) | Read | Show HN traction (points, comments) and Ask HN threads. |
| [Apify Store API](https://api.apify.com/v2/store?limit=100&sortBy=popularity) | Read | Actor usage and ratings as JSON; cheaper than web searches. Add `&search=<term>`. |
| [CodeCanyon search](https://codecanyon.net/search/zatca) | Read | Sales counts for any niche term (replace the term). |
| [G2](https://www.g2.com/categories/marketing-automation) | Read | Category leaders with review counts; read 1 to 3 star reviews. |
| [Capterra](https://www.capterra.com/customer-service-software/) | Read | Same as G2, with more SMB and vertical categories. |
| [Trustpilot](https://www.trustpilot.com/categories/software_company) | Read | Complaints with review counts. |
| [AlternativeTo](https://alternativeto.net/) | Read | "Alternative to X" searches show which tools people want to leave. |
| [SaaSHub](https://www.saashub.com/) | Read | Category leaderboards and alternatives. |
| [BiggerPockets forums](https://www.biggerpockets.com/forums) | Read | Real estate investor and landlord threads with reply counts. |
| [Upwork jobs](https://www.upwork.com/nx/search/jobs/?q=automation) | Read | Repeated job titles with budgets show spending on a problem. |
| [Fiverr categories](https://www.fiverr.com/categories/programming-tech/ai-coding) | Read | Gigs with prices and review counts. |
| [hnhiring](https://hnhiring.com/) | Partial | Job counts by technology from HN "Who is hiring"; no individual posts. |
| Shopify Community, ContractorTalk, RemoteOK, Etsy | Search | Blocked, paywalled or JavaScript. |

### Trends and momentum
| Source | Access | Use it for |
|---|---|---|
| [Exploding Topics](https://explodingtopics.com/) | Read | Free trending topics with volume and growth (for example "Secops" 8.1K volume, +163%). |
| [GitHub trending](https://github.com/trending) | Read | Stars gained today. |
| [Product Hunt](https://www.producthunt.com/) | Partial | Today's launches; upvote counts may be incomplete. |
| [Marketplace Pulse](https://www.marketplacepulse.com/articles) | Read | Amazon, TikTok Shop, Walmart and Etsy seller trends. |
| [SteamDB charts](https://steamdb.info/charts/) | Read | Player counts, for entertainment tooling ideas (not in-game sales). |
| [Graphtreon](https://graphtreon.com/top-patreon-creators) | Read | Creator earnings and paid members. |
| [Skool discovery](https://www.skool.com/discovery) | Read | Paid communities with member counts and prices. |
| IdeaBrowser, Pinterest Trends, Y Combinator directory, Substack leaderboards | Search | Blocked, 403 or JavaScript. |

### News, regulation and platform shifts ("what change forces people to buy something new?")
Every run starts here (PROMPT.md step 1). Tested 2026-09-25.

**Laws, rules and regulators**
| Source | Access | Use it for |
|---|---|---|
| [Federal Register API](https://www.federalregister.gov/api/v1/documents.json?conditions[type][]=RULE&order=newest&per_page=20) | Read | Newest US final rules with agency and date. Search by topic with `conditions[term]=`, for example `%22artificial+intelligence%22`, `privacy`, `accessibility`, `small+business`. Use `conditions[type][]=PRORULE` for proposed rules. |
| [FTC press releases](https://www.ftc.gov/news-events/news/press-releases) | Read | US consumer protection actions and new rules (subscriptions, reviews, pricing, AI claims). |
| [Digital Policy Alert](https://digitalpolicyalert.org/) | Read | Global tech policy events with jurisdiction and date (AI, data, platforms, cybersecurity). |
| [IAPP news](https://iapp.org/news/) | Read | Privacy and AI governance news worldwide. The IAPP state AI law tracker is members-only. |
| [EU AI Act timeline](https://artificialintelligenceact.eu/implementation-timeline/) | Read | Upcoming AI Act obligations by date. |
| [White & Case AI Watch](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker) | Read | AI regulation status by country; few dates, so use it for orientation. |
| [gov.uk news and communications](https://www.gov.uk/search/news-and-communications?order=updated-newest) | Read | UK government and regulator announcements, newest first. |
| [VATupdate](https://www.vatupdate.com/category/saudi-arabia/) | Read | E-invoicing and tax-reporting rules by country (change the category for UAE, EU countries and others). |
| EUR-Lex, EU Commission press corner, ICO news, legislation.gov.uk | Search | JavaScript pages or incomplete listings. |
| Google News RSS | Search | Blocked by robots.txt. Use web search with dates instead. |

**Platform and AI changes**
| Source | Access | Use it for |
|---|---|---|
| [Shopify developer changelog](https://shopify.dev/changelog) | Read | Deprecations and new APIs, with dates. |
| [HubSpot developer changelog](https://developers.hubspot.com/changelog) | Read | Sunsets and new APIs, with dates. |
| [Google Search Central blog](https://developers.google.com/search/blog) | Read | Search and ranking policy changes affecting site owners. |
| [Apple developer news](https://developer.apple.com/news/) | Read | App Store rule and platform changes. |
| [OpenAI news](https://openai.com/news/) and [Anthropic news](https://www.anthropic.com/news) | Read | New AI capabilities that make manual jobs automatable. |
| [Meta Graph API changelog](https://developers.facebook.com/docs/graph-api/changelog/) | Partial | Version dates only. |
| Google Ads API release notes, WhatsApp Business Platform changelog, Chrome Platform Status, Stripe changelog, QuickBooks and Xero developer news | Untested | Try them and report access in the brief. |

**Tech and money news**
| Source | Access | Use it for |
|---|---|---|
| [Techmeme](https://www.techmeme.com/) | Read | The day's biggest tech stories with sources. |
| [TechCrunch feed](https://techcrunch.com/feed/) | Read | Startup launches, funding and shutdowns, with dates. |
| [Crunchbase News](https://news.crunchbase.com/) | Read | Funding rounds by sector: where investors see money. |
| [Hacker News front page](https://news.ycombinator.com/) | Read | What developers are reacting to. |

**Web search patterns for news (use dates in queries)**
- `"new rule" OR "final rule" OR "comes into force" small businesses {month} {year}`
- `"compliance deadline" {year+1} software OR "online businesses"`
- `"AI Act" OR "AI law" obligations {month} {year}`, and the same for "state AI law", "privacy law" and "accessibility law"
- `{platform} "deprecat" OR "sunset" OR "shutting down" {month} {year}`, for Shopify, HubSpot, Google, Meta, WhatsApp, Microsoft, Atlassian, Salesforce, Zapier, Notion, QuickBooks, Xero
- `"shutting down" OR "sunsetting" SaaS customers {month} {year}`: stranded paying customers need a replacement
- `"e-invoicing" mandate {country} {year}`, `"price increase" {tool} customers angry {year}`

## 4. How a run should use this

PROMPT.md "WHERE TO LOOK" is the authoritative order. In short:

1. **News and regulation scan** using the news section above, feeding DEADLINES.md.
2. **Wide scan** of all 27 sectors, logging each sector's strongest signal.
3. **Proven models:** start from the revenue and exit sources and marketplace leaders, then ask where the same model is missing (another platform, segment, language or country).
4. **Source notes:** record which sources produced candidates and which failed, so this library can be pruned.

## 5. Rules

- Do not use connectors that spend credits (Lusha, Vibe Prospecting, lemlist) in scheduled runs.
- The Meta Ads connector's ad library search needs an active Meta ad account (it worked on Sep 25, 2026). Keep it to a few searches per run.
- Never bulk-scrape, and never work around blocks or robots.txt. When a site blocks the fetch tool, use web search.
