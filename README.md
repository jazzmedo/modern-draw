# Draw.io College Subjects — Summaries & Rules

A personal collection of `.drawio` summaries, rule sheets, and study aids for Computer Science courses at Modern Academy.

## ⚠️ Disclaimer

**This repository is NOT official course material from Modern Academy.**
It is a set of personal study notes made by a student to help revise. Content may be incomplete, simplified, or wrong in places. Always verify against your official lecture material before relying on anything here. Use at your own risk.

## How to browse

Open `index.html` in any browser. The page lists every diagram grouped by year/term and gives you three actions per file:

- **Open in draw.io** — opens the file editable in [app.diagrams.net](https://app.diagrams.net).
- **Quick view** — opens a read-only viewer (no account required).
- **Download** — saves the raw `.drawio` file.

The "open" links pull files from `raw.githubusercontent.com`, so they work for anyone visiting the page (no clone required) as long as the repo is public.

## Repository structure

```
2nd Subjects/        Year 2 diagrams (+ SummerCourse subfolder)
3rd Subjects/
  Term1/             Year 3, Term 1
  Term2/             Year 3, Term 2 (+ Cyber, Modeling subfolders)
4th Subjects/
  Term 1/            Year 4, Term 1
Others/              Personal draw.io config / scratch — NOT study material
index.html           The gallery page
scripts/             Helper scripts
```

## Importing the Scratchpad into draw.io

The Scratchpad is the persistent shape tray that sits at the top of draw.io's left sidebar. The file `Others/Scratchpad.xml` is a saved copy of mine — here's how to load it into your own draw.io.

### Option A — Replace your scratchpad (recommended)

This swaps your current scratchpad with the contents of the file.

1. Open [app.diagrams.net](https://app.diagrams.net) and start (or open) any diagram.
2. Make the Scratchpad panel visible: top menu **View → Scratchpad** (toggle it on if it's hidden). It appears at the top of the left sidebar.
3. Hover the **Scratchpad** header in the sidebar and click the **pencil / edit** icon (✏️) on the right.
4. The "Edit Scratchpad" dialog opens with the raw XML.
5. Open `Others/Scratchpad.xml` in any text editor, copy its full contents, and paste it into the dialog (replacing whatever is there).
6. Click **OK**. The shapes appear immediately in the Scratchpad panel.

> Tip: scratchpad data lives in your browser's `localStorage` under the key `.scratchpad` for `app.diagrams.net`, so it persists across sessions but is per-browser/per-device.

### Option B — Load it as a custom shape library

Use this if you want to keep your existing scratchpad and just have these shapes available alongside it.

1. Open [app.diagrams.net](https://app.diagrams.net).
2. Top menu **File → Open Library from → Device…**
3. Select `Others/Scratchpad.xml` from this repo.
4. The shapes show up as a new section at the bottom of the left sidebar. Right-click any shape → **Add to Scratchpad** if you want it pinned.

### Importing the config (optional)

`Others/Drawio.config.json` is my editor preferences (theme, grid, default fonts, etc.). To use it: in draw.io, top menu **Extras → Configuration…**, paste the JSON, click **Apply**, then reload.

## Adding a new diagram

1. Drop the `.drawio` file into the appropriate year/term folder.
2. Regenerate the gallery file list:
   ```bash
   python3 scripts/build-gallery.py
   ```
3. Commit and push.

The script rewrites the embedded file list inside `index.html` between the `<!-- FILES:START -->` / `<!-- FILES:END -->` sentinels.
