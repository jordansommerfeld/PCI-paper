#!/usr/bin/env python3
"""
Generate a simple sitemap.xml that lists index.html and the PDF.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

BASE = "https://www.pciprinciple.org"

pages = [
    f"{BASE}/index.html",
    f"{BASE}/PCI_Final.pdf"
]

urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for url in pages:
    u = ET.SubElement(urlset, "url")
    loc = ET.SubElement(u, "loc")
    loc.text = url

tree = ET.ElementTree(urlset)
tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
print("sitemap.xml written with", len(pages), "entries")
