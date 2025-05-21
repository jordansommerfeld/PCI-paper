#!/usr/bin/env python3
"""
Ensure basic SEO meta tags exist in index.html (or index.md rendered as HTML).
Very naive string-based insert; good enough for static page.
"""

import pathlib
file = pathlib.Path("index.html")
if not file.exists():
    print("index.html not found; skipping")
    exit(0)

html = file.read_text()
meta_block = """
<meta name="description" content="Finite-measure fix to the Boltzmann-brain paradox.">
<link rel="canonical" href="https://pciprinciple.org/">
<meta property="og:title" content="Principle of Counterbalanced Infinity">
<meta property="og:description" content="Information-theoretic cosmology paper by Jordan Sommerfeld">
<meta property="og:image" content="https://pciprinciple.org/fig1.png">
"""

if "og:title" not in html:
    html = html.replace("<head>", "<head>" + meta_block.strip())
    file.write_text(html)
    print("Meta tags inserted")
else:
    print("Meta tags already present")
