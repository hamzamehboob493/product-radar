#!/usr/bin/env python3
"""Post newly added digests/*.md files to a Discord webhook.

On a push: posts every digest file added by that push.
On a manual run (workflow_dispatch): re-posts the most recent digest.
Uses only the Python standard library.
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

WEBHOOK = os.environ.get("DISCORD_WEBHOOK", "").strip()
BEFORE = os.environ.get("BEFORE", "").strip()
EVENT = os.environ.get("GITHUB_EVENT_NAME", "")
MAX_CHARS = 1900  # Discord's hard limit is 2000 per message
NULL_SHA = "0" * 40


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def md_files(output: str) -> list[str]:
    return sorted(line.strip() for line in output.splitlines() if line.strip().endswith(".md"))


def digests_to_post() -> list[str]:
    if EVENT == "workflow_dispatch":
        return md_files(git("ls-files", "digests"))[-1:]
    if BEFORE and BEFORE != NULL_SHA:
        return md_files(git("diff", "--name-only", "--diff-filter=A", BEFORE, "HEAD", "--", "digests"))
    # First push to the branch: nothing to diff against, use the files added in HEAD.
    return md_files(git("show", "--name-only", "--diff-filter=A", "--pretty=format:", "HEAD", "--", "digests"))


def split(text: str) -> list[str]:
    """Split into Discord messages.

    A line containing only '---' starts a new message, so each section (for
    example one idea card) arrives as its own message. Sections longer than
    MAX_CHARS are split on line breaks without losing text.
    """
    chunks: list[str] = []
    section: list[str] = []
    for line in text.strip().split("\n"):
        if line.strip() == "---":
            chunks.extend(split_section("\n".join(section)))
            section = []
        else:
            section.append(line)
    chunks.extend(split_section("\n".join(section)))
    return chunks


def split_section(text: str) -> list[str]:
    """Split one section on line breaks into chunks of at most MAX_CHARS."""
    chunks: list[str] = []
    buf = ""

    def flush() -> None:
        nonlocal buf
        if buf.strip():
            chunks.append(buf)
        buf = ""

    for line in text.strip().split("\n"):
        while len(line) > MAX_CHARS:
            flush()
            chunks.append(line[:MAX_CHARS])
            line = line[MAX_CHARS:]
        if buf and len(buf) + len(line) + 1 > MAX_CHARS:
            flush()
        buf = f"{buf}\n{line}" if buf else line
    flush()
    return chunks


def post(content: str) -> None:
    body = json.dumps({"content": content, "allowed_mentions": {"parse": []}}).encode()
    for _ in range(6):
        req = urllib.request.Request(
            WEBHOOK,
            data=body,
            method="POST",
            headers={"Content-Type": "application/json", "User-Agent": "ProductRadar/1.0 (+github-actions)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30):
                return
        except urllib.error.HTTPError as err:
            detail = err.read()
            if err.code == 429:
                try:
                    wait = float(json.loads(detail or b"{}").get("retry_after", 2))
                except ValueError:
                    wait = 2.0
                time.sleep(wait + 0.5)
                continue
            sys.exit(f"Discord returned HTTP {err.code}: {detail[:300]!r}")
    sys.exit("Gave up after repeated Discord rate limits")


def main() -> None:
    if not WEBHOOK:
        sys.exit("DISCORD_WEBHOOK secret is not set (repo Settings > Secrets and variables > Actions).")
    files = digests_to_post()
    if not files:
        print("No new digest files in this push; nothing to post.")
        return
    for path in files:
        with open(path, encoding="utf-8") as fh:
            chunks = split(fh.read())
        for chunk in chunks:
            post(chunk)
            time.sleep(1)
        print(f"Posted {path} in {len(chunks)} message(s).")


if __name__ == "__main__":
    main()
