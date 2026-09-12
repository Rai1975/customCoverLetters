"""
job_scraper.py

Scrapes a job posting page and extracts (title, description text).
"""

import sys
import json
import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    # A normal browser-like user agent avoids some basic bot-blocking.
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


def fallback_title(soup: BeautifulSoup):
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find("h1")
    return h1.get_text(strip=True) if h1 else None


def fallback_description(soup: BeautifulSoup):
    """
    Heuristic: find the largest block of text on the page,
    stripping nav/header/footer/script/style noise.
    """
    for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
        tag.decompose()

    candidates = soup.find_all(["article", "main", "section", "div"])
    best, best_len = None, 0
    for c in candidates:
        text = c.get_text(separator="\n", strip=True)
        if len(text) > best_len:
            best, best_len = text, len(text)

    if best:
        # collapse excessive blank lines
        return re.sub(r"\n{3,}", "\n\n", best)
    return soup.get_text(separator="\n", strip=True)


def scrape_job(url: str) -> dict:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")

    title = fallback_title(soup)
    description = fallback_description(soup)

    return {
        "url": url,
        "title": title,
        "description": description,
    }


def scrape(url, out=None):
    try:
        result = scrape_job(url)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    if out:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Saved to {out}")
    else:
        return json.dumps(result, indent=2, ensure_ascii=False)