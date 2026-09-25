# Product Radar

A scheduled Claude task researches micro product gaps and bigger AI-assisted builds for Engisols, screens them through nine rejection gates, and commits the results here. A GitHub Action posts each new digest to Discord.

## How it works

1. On schedule, Claude clones this repo, reads `PROMPT.md` and follows it.
2. Each run commits three things in one commit:
   - `briefs/YYYY-MM-DD.md`: the full decision-ready brief
   - `digests/YYYY-MM-DD.md`: the short Discord summary, linking to the brief
   - a new row per screened idea in `ideas-index.md`
3. `.github/workflows/discord.yml` fires on any new file in `digests/` and posts it to the Discord webhook stored in the `DISCORD_WEBHOOK` repo secret, split to fit Discord's 2,000 character limit.

## Changing what the radar looks for

Edit `PROMPT.md` (rules, gates, output format) or `SOURCES.md` (sectors and source library). The scheduled task only says "clone the repo and follow PROMPT.md", so changes apply from the next run without touching the schedule. Every run scans all 27 sectors in `SOURCES.md`, then screens the 8 to 12 strongest candidates through the gates.

## Re-sending a digest

Actions tab > "Post digest to Discord" > Run workflow. That re-posts the most recent digest.

## Obsidian

Open this folder as a vault. Briefs, digests and the index are plain markdown. The Obsidian Git community plugin can pull new runs automatically.

## Setup checklist

- Repo secret `DISCORD_WEBHOOK` = the Discord channel webhook URL (Settings > Secrets and variables > Actions).
- Actions enabled for the repo.
