# SampadaHita

Redesigned marketing site for **SampadaHita** — *"Well-Wisher of Your Wealth."*
Education-first wealth management: free financial analysis, advanced tax strategy,
retirement, investment, and legacy planning for families and high earners.

## Structure
Self-contained, responsive static pages (inline CSS + self-hosted subsetted
WOFF2 fonts — no external requests). Light & dark themes.

| Page | File |
|------|------|
| Home | `index.html` |
| About | `about.html` |
| Services | `services.html` |
| Tax Strategies | `tax-strategies.html` |
| Who We Serve | `who-we-serve.html` |
| Partnership | `partnership.html` |
| Resources | `resources.html` |
| Contact | `contact.html` |

## Editing
Source lives in `src/`. Edit `src/style.css` or the fragments in `src/pages/`,
then rebuild:

```
python3 src/build.py
```

This regenerates every page at the repo root with the shared nav, footer, CSS,
and fonts inlined.

Design system: deep navy + premium gold + warm cream · Outfit (display) +
Work Sans (body).
