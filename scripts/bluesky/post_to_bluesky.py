#!/usr/bin/env python3
"""
Bluesky Auto-Poster for Jekyll Blog

Fetches new posts from the Jekyll RSS feed and posts them to Bluesky.
Tracks posted entries to avoid duplicates.
"""

import os
import json
import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path

import feedparser
from atproto import Client

# Configuration
SITE_URL = "https://hawksley.org"
RSS_FEED_URL = f"{SITE_URL}/feed.xml"
POSTED_ENTRIES_FILE = Path(__file__).parent / "posted_entries.json"


def load_posted_entries():
    """Load the list of already posted entries."""
    try:
        if POSTED_ENTRIES_FILE.exists():
            with open(POSTED_ENTRIES_FILE, "r") as f:
                return json.load(f)
        return {}
    except Exception as e:
        print(f"Error loading posted entries: {e}")
        return {}


def save_posted_entries(posted_entries):
    """Save the list of posted entries."""
    try:
        with open(POSTED_ENTRIES_FILE, "w") as f:
            json.dump(posted_entries, f, indent=2)
    except Exception as e:
        print(f"Error saving posted entries: {e}")


def create_post_with_link(client, title, url):
    """
    Create a Bluesky post with a clickable link.

    Format: "New blog post: {title}\n\n{url}"
    """
    # Build the post text
    post_text = f"New blog post: {title}"
    link_section = f"\n\n{url}"
    full_text = post_text + link_section

    # Ensure we don't exceed Bluesky's character limit (300 chars)
    if len(full_text) > 300:
        # Truncate title if needed
        max_title_len = 300 - len(link_section) - len("New blog post: ") - 3  # 3 for "..."
        truncated_title = title[:max_title_len] + "..."
        post_text = f"New blog post: {truncated_title}"
        full_text = post_text + link_section

    # Calculate byte positions for the link facet
    post_text_bytes = post_text.encode("utf-8")
    link_prefix = "\n\n"
    url_bytes = url.encode("utf-8")

    link_start = len(post_text_bytes) + len(link_prefix.encode("utf-8"))
    link_end = link_start + len(url_bytes)

    # Create facet for clickable link
    facets = [
        {
            "index": {"byteStart": link_start, "byteEnd": link_end},
            "features": [{"$type": "app.bsky.richtext.facet#link", "uri": url}],
        }
    ]

    print(f"Posting: {full_text}")

    # Post to Bluesky
    response = client.send_post(text=full_text, facets=facets)
    return response


def main():
    print("=== Bluesky Auto-Poster Starting ===")
    print(f"RSS Feed: {RSS_FEED_URL}")

    # Check for required environment variables
    bluesky_handle = os.environ.get("BLUESKY_HANDLE")
    bluesky_password = os.environ.get("BLUESKY_PASSWORD")

    if not bluesky_handle or not bluesky_password:
        print("Error: BLUESKY_HANDLE and BLUESKY_PASSWORD environment variables must be set.")
        print("Add these as repository secrets in Settings > Secrets and variables > Actions")
        return

    # Initialize Bluesky client and login
    client = Client()
    print(f"Logging in as: {bluesky_handle}")

    try:
        client.login(bluesky_handle, bluesky_password)
        print("Login successful!")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # Fetch and parse RSS feed
    print(f"\nFetching RSS feed...")
    feed = feedparser.parse(RSS_FEED_URL)

    if not feed.entries:
        print("No entries found in feed.")
        return

    print(f"Found {len(feed.entries)} entries in feed.")

    # Load previously posted entries
    posted_entries = load_posted_entries()
    print(f"Previously posted: {len(posted_entries)} entries")

    new_posts_count = 0

    for entry in feed.entries:
        title = entry.get("title", "").strip()
        link = entry.get("link", "")

        if not link:
            print(f"Skipping entry with no link: {title}")
            continue

        # Create unique ID from the link
        entry_id = hashlib.md5(link.encode()).hexdigest()

        if entry_id in posted_entries:
            print(f"Already posted: {title}")
            continue

        print(f"\n--- New post found: {title} ---")

        try:
            response = create_post_with_link(client, title, link)

            # Record successful post
            posted_entries[entry_id] = {
                "title": title,
                "link": link,
                "date_posted": datetime.now(timezone.utc).isoformat(),
                "post_uri": getattr(response, "uri", "Unknown"),
            }

            new_posts_count += 1
            print(f"Successfully posted! URI: {posted_entries[entry_id]['post_uri']}")

            # Save after each successful post
            save_posted_entries(posted_entries)

            # Wait between posts to avoid rate limiting
            time.sleep(2)

        except Exception as e:
            print(f"Error posting '{title}': {e}")

    print(f"\n=== Complete: Posted {new_posts_count} new entries ===")


if __name__ == "__main__":
    main()
