#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

BASE_DIR = Path(".")

def get_frequency_key(seconds: int) -> str:
    if seconds <= 60:
        return f"high_{seconds}s"
    elif seconds <= 900:
        return f"medium_{seconds//60}m"
    else:
        return f"low_{seconds//60}m"

def create_or_update_scraper(frequency_seconds: int, searches: list, name: str = None):
    # ... (full implementation with lock and supervisor)
    print("Scraper management complete")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frequency", type=int, required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--name", default=None)
    args = parser.parse_args()

    search = {"name": args.name or f"Suche_{args.frequency}s", "url": args.url, "recursive": True}
    create_or_update_scraper(args.frequency, [search])
