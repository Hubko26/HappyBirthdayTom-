#!/bin/bash
# Builds a standalone puzzle.html with both images embedded as base64 data URIs.
# Run from the TestApp directory: bash build_standalone.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ANIME="$SCRIPT_DIR/AnimeVersion.png"
ORIGINAL="$SCRIPT_DIR/OriginalVersion.png"
TEMPLATE="$SCRIPT_DIR/templates/index.html"
OUTPUT="$SCRIPT_DIR/puzzle.html"

echo "Encoding images..."
ANIME_B64="data:image/png;base64,$(base64 -i "$ANIME")"
ORIG_B64="data:image/png;base64,$(base64 -i "$ORIGINAL")"

echo "Building standalone HTML..."
sed \
  -e "s|/static/puzzle.png|$ANIME_B64|g" \
  -e "s|/static/reveal.png|$ORIG_B64|g" \
  "$TEMPLATE" > "$OUTPUT"

SIZE=$(wc -c < "$OUTPUT" | tr -d ' ')
echo "Done! Created $OUTPUT ($(( SIZE / 1024 / 1024 ))MB)"
echo "Double-click puzzle.html to play — no server needed."
