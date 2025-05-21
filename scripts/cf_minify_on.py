#!/usr/bin/env python3
"""
Enable HTML, CSS, and JS minification (and Brotli, if desired) on Cloudflare
for the pci­principle.org zone. Extend this file to add Cache Rules, Early
Hints, etc. as needed.
"""

import os
import requests
import sys
import json

CF_API = os.environ["CF_API"]               # comes from GitHub secret
ZONE_ID = "76d618e5ceb641697b69aa09af4e6d72"  # your zone ID

headers = {
    "Authorization": f"Bearer {CF_API}",
    "Content-Type": "application/json"
}

def patch(setting: str, value):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/settings/{setting}"
    r = requests.patch(url, headers=headers, json={"value": value})
    if not r.ok:
        print(f"Error {setting}: {r.status_code} → {r.text}")
        sys.exit(1)
    print(f"{setting}: success")

if __name__ == "__main__":
    # Turn on HTML/CSS/JS auto-minify
    patch("minify", {"css": "on", "js": "on", "html": "on"})
    # (Brotli is on by default for free zones; no endpoint needed)
