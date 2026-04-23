#!/usr/bin/env python3
"""Builds a standalone puzzle.html with both images embedded as base64 data URIs."""

import base64
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ANIME = os.path.join(SCRIPT_DIR, "AnimeVersion.png")
ORIGINAL = os.path.join(SCRIPT_DIR, "OriginalVersion.png")
TEMPLATE = os.path.join(SCRIPT_DIR, "templates", "index.html")
OUTPUT = os.path.join(SCRIPT_DIR, "puzzle.html")


def encode_image(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


print("Encoding images...")
anime_b64 = encode_image(ANIME)
orig_b64 = encode_image(ORIGINAL)

print("Building standalone HTML...")
with open(TEMPLATE, "r") as f:
    html = f.read()

html = html.replace("/static/puzzle.png", anime_b64)
html = html.replace("/static/reveal.png", orig_b64)

with open(OUTPUT, "w") as f:
    f.write(html)

size_mb = os.path.getsize(OUTPUT) / 1024 / 1024
print(f"Done! Created {OUTPUT} ({size_mb:.1f}MB)")
print("Double-click puzzle.html to play - no server needed.")
