# -*- coding: utf-8 -*-
"""index.html előállítása a canvas-forrásból.

A `Wildland Concepts.dc.html` a szerkeszthető forrás (Claude Design canvas).
A publikált `index.html` ugyanaz, csak a <head> ki van egészítve címmel,
faviconnal és OG-metákkal, amiket a canvas nem tartalmaz.

Használat:  python build.py
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "Wildland Concepts.dc.html")
DST = os.path.join(HERE, "index.html")

OLD_HEAD = """<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="./support.js"></script>"""

NEW_HEAD = """<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wildland Concepts — Túlélés, erdészeti és vadászati képzések</title>
<meta name="description" content="Wildland Concepts — túlélő, erdészeti és vadászati képzések, felszerelések és Black Forest programok.">
<link rel="icon" href="logo-transparent.png" type="image/png">
<meta property="og:title" content="Wildland Concepts">
<meta property="og:description" content="Túlélő, erdészeti és vadászati képzések, felszerelések és Black Forest programok.">
<meta property="og:image" content="logo-transparent.png">
<meta property="og:type" content="website">
<script src="./support.js"></script>"""

src = io.open(SRC, encoding="utf-8").read()

if OLD_HEAD not in src:
    sys.exit(
        "HIBA: a canvas <head> blokkja nem a várt formátumú.\n"
        "A build.py OLD_HEAD konstansát kell hozzáigazítani a forráshoz."
    )

io.open(DST, "w", encoding="utf-8", newline="").write(src.replace(OLD_HEAD, NEW_HEAD, 1))
print("index.html frissítve a canvas-forrásból ({:,} bájt)".format(os.path.getsize(DST)))
