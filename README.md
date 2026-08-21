# Wildland Concepts — redesign

Statikus egyoldalas (SPA) weboldal, Claude Design canvas (`.dc.html`) formátumból építve.

## Felépítés

| Fájl | Szerep |
| --- | --- |
| `index.html` | A teljes oldal (7 aloldal: Kezdőlap, Rólunk, Képzéseink, Felszerelések, Black Forest, Galéria, Árlista, Kapcsolat) |
| `support.js` | Claude Design runtime — a `<x-dc>` sablont React 18-cal rendereli (React UMD unpkg CDN-ről töltődik) |
| `logo-transparent.png` | Logó / favicon |
| `uploads/` | Helyi képek |
| `Wildland Concepts.dc.html` | Az eredeti canvas-forrás (szerkesztéshez, nem publikált oldal) |

## Futtatás helyben

```bash
npx serve .
```

Sima fájlmegnyitás (`file://`) nem elég, mert a runtime CDN-ről tölt.

## Deploy

Vercel, statikus (framework: Other), build parancs nélkül, output = repó gyökere.

## Ismert tudnivaló

A Galéria és néhány kép a régi élő oldalról (`www.wildlandconcepts.com`) hivatkozik. Ha a régi oldal megszűnik, ezeket le kell tölteni az `uploads/` mappába.
