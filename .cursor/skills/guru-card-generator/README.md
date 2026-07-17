# Guru Card Generator — SA Team Guide

Turn customer-specific solution docs into generalized [Customer Solutions Knowledge Base (CSKB)](https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base) cards using Cursor.

**Repo:** https://github.com/rebecca-iterable/sa-solutions-toolkit

---

## Slack blurb (copy-paste)

```
:new: Guru Card Generator in Cursor — turn solution docs into CSKB cards faster

Clone sa-solutions-toolkit (https://github.com/rebecca-iterable/sa-solutions-toolkit), connect Guru MCP, and ask Cursor to generalize a solutions doc. It will:
• Anonymize customer details
• Map content to our Guru template (Purpose, Problem, Solution, etc.)
• Save screenshots to examples/<pattern>/images/ with borders applied
• Create a WIP: draft in Guru via MCP

You finish: CSKB collection + folder, upload bordered images, tags, verifier, publish (~5–10 min vs writing from scratch).

Setup (one time):
1. Clone repo (or copy .cursor/skills/guru-card-generator into your project)
2. Open your project in Cursor
3. Add Guru MCP to ~/.cursor/mcp.json → { "mcpServers": { "Guru": { "url": "https://mcp.api.getguru.com/mcp" } } }
4. Restart Cursor, authenticate Guru
5. Optional: pip install pillow (screenshot borders only)

Prompt: "Generalize this solutions doc and create a Guru draft in CSKB."

Input: paste text, upload PDF/DOCX, or point to a local file. Google Doc links alone won't work — export or paste content.

Reference example: .cursor/skills/guru-card-generator/examples/statsig-journey-live-data/
Full guide: .cursor/skills/guru-card-generator/README.md
```

---

## What it does

| Automated | Manual (in Guru) |
|-----------|------------------|
| Anonymize customer names, IDs, metrics | Move draft to **Customer Solutions Knowledge Base** |
| Generalize deal language → reusable guidance | Choose folder, tags (max 4), verifier |
| Map to CSKB template sections | Paste into template fields if styles are flat |
| Border screenshots (`*-bordered.png`) | Upload bordered images |
| Save local files under `examples/<pattern>/` | Remove `WIP:` from title and publish |
| Create Guru draft via MCP | — |

## Prerequisites

- **Cursor** installed
- **Guru access** with permission to create drafts in [Customer Solutions Knowledge Base (CSKB)](https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base)
- **Guru MCP** connected (optional but recommended — without it, Cursor still generalizes the doc but won't auto-create a Guru draft)

Share the **entire** `guru-card-generator/` folder, not just `SKILL.md`. The agent needs `guru-template.md`, `guru-config.md`, and `scripts/` too.

## Get the skill

### Option A — Clone the repo and open in Cursor (recommended)

Use this if you want the skill, examples, and future updates in one place.

```bash
git clone https://github.com/rebecca-iterable/sa-solutions-toolkit.git
cd sa-solutions-toolkit
```

In Cursor: **File → Open Folder** → select the `sa-solutions-toolkit` folder.

The skill is already at `.cursor/skills/guru-card-generator/` — no extra copy step. Open any chat in this project and prompt.

To pull updates later: `git pull`

### Option B — Add the skill to an existing Cursor project

Use this if you already work in another repo and only want the Guru card skill there.

```bash
git clone https://github.com/rebecca-iterable/sa-solutions-toolkit.git /tmp/sa-solutions-toolkit
cp -r /tmp/sa-solutions-toolkit/.cursor/skills/guru-card-generator \
  /path/to/your-project/.cursor/skills/
```

Your project should look like:

```
your-project/
└── .cursor/
    └── skills/
        └── guru-card-generator/
            ├── SKILL.md
            ├── guru-template.md
            ├── guru-config.md
            ├── docs/solution-template.md
            ├── scripts/
            └── examples/
```

Create `.cursor/skills/` if it doesn't exist. Open **your project** in Cursor (not the toolkit repo).

### Option C — Personal skill (works in any project)

Install once; use in every Cursor project without copying into each repo.

```bash
git clone https://github.com/rebecca-iterable/sa-solutions-toolkit.git /tmp/sa-solutions-toolkit
cp -r /tmp/sa-solutions-toolkit/.cursor/skills/guru-card-generator ~/.cursor/skills/
```

Restart Cursor. The skill is available no matter which folder you have open.

### Zip install (no git)

If you received `guru-card-generator.zip`, unzip and place the folder at one of:

- `your-project/.cursor/skills/guru-card-generator/` (Option B)
- `~/.cursor/skills/guru-card-generator/` (Option C)

After unzipping, confirm the path ends with `guru-card-generator/SKILL.md` (not nested twice).

---

## One-time setup

After the skill is installed (Option A, B, or C):

1. **Connect Guru MCP** — **merge** into `~/.cursor/mcp.json` (don't replace the whole file if you already have other MCP servers like Iterable):

   ```json
   {
     "mcpServers": {
       "Guru": { "url": "https://mcp.api.getguru.com/mcp" }
     }
   }
   ```

   Restart Cursor and authenticate when prompted. Confirm Guru appears under **Cursor Settings → MCP**.

2. **Optional — Pillow** (only if your docs include screenshots that need borders):

   ```bash
   pip install pillow
   ```

3. **Skim the reference example** — [examples/statsig-journey-live-data/](examples/statsig-journey-live-data/) shows before/after quality for one Journey pattern. Other Iterable features (campaigns, catalog, data feeds, etc.) follow the same workflow.

## Quick start

End-to-end flow once the skill is installed:

1. **Open your project** in Cursor (cloned repo, project with copied skill, or any project if using `~/.cursor/skills/`)
2. **Paste or upload** a solutions doc (PDF, DOCX, markdown, or pasted text)
3. **Prompt:** *"Generalize this solutions doc and create a Guru draft in CSKB."*
4. **Upload screenshots** in chat if Cursor asks (UI setup steps with no images attached)
5. **Open the Guru draft link** Cursor returns — finish in Guru (collection, folder, images, tags, publish)

To update the skill later: `git pull` if you cloned the repo, or re-copy the folder if you installed via zip/copy.

## How to use

### Prompts that work

- *"Generalize this solutions doc and create a Guru draft in CSKB."*
- *"Turn this into a Guru card for the Customer Solutions Knowledge Base."*
- *"Anonymize this and post a Guru draft."*

To skip Guru MCP: *"Generalize only — don't create a Guru draft yet."*

### Input formats

| Works | Doesn't work alone |
|-------|-------------------|
| Pasted text / markdown | Google Doc share link |
| Uploaded PDF or DOCX | — |
| Local file path in repo | — |
| Google Doc export (PDF/DOCX) | — |

If the doc has UI walkthrough steps but no screenshots, Cursor will ask you to upload them.

### Writing new solution docs

Use [docs/solution-template.md](docs/solution-template.md) as the input structure — it maps cleanly to the Guru card template.

## What you get after a run

| Output | Location |
|--------|----------|
| Guru draft link | Returned in chat — title prefixed with `WIP:` |
| Generalized card markdown | `examples/<pattern-name>/output-guru-card.md` |
| Screenshots (if any) | `examples/<pattern-name>/images/` (originals + `*-bordered.png`) |

Cursor also searches Guru for duplicate cards before creating a new draft.

## After Cursor creates the draft

1. Open the draft from **My Drafts** in Guru
2. Set collection → **Customer Solutions Knowledge Base**
3. Choose the correct folder
4. Paste content **section by section** into template fields (don't bulk-paste — preserves heading styles)
5. Upload images from `examples/<pattern>/images/*-bordered.png`
6. Add tags, set verifier, remove `WIP:` from title, publish

**Redact secrets** in screenshots (API keys, account IDs) before uploading.

## Screenshots and images

When UI walkthrough content is detected, Cursor will:

1. Ask for screenshots (journey canvas, webhook config, etc.)
2. Save originals to `examples/<pattern-slug>/images/`
3. Run `python scripts/add-image-borders.py examples/<pattern-slug>/images/`
4. Embed `*-bordered.png` in the local markdown

Guru cannot add borders in the editor — always upload the bordered copies.

## Title format

`[Pattern name]: [Iterable capability] + [Integration/partner if any]`

Examples:
- Real-time Experiment Assignment: Journey Live Data + Statsig
- Catalog-Based Product Recommendations: Data Feeds + Shopify
- Post-Purchase Cross-Sell: Triggered Campaign + Segment

## Contribute examples

When you document a new pattern, keep the generated files:

```
examples/your-pattern-name/
  input-solution-doc.md
  output-guru-card.md
  images/          # originals + *-bordered.png
```

See [examples/README.md](examples/README.md).

## Troubleshooting

| Issue | What to do |
|-------|------------|
| Skill doesn't run | Confirm `guru-card-generator/SKILL.md` exists at `.cursor/skills/` (project) or `~/.cursor/skills/` (personal) |
| No Guru draft created | Check **Cursor Settings → MCP** — Guru should be connected. Restart Cursor after editing `mcp.json` |
| Lost other MCP servers | You may have replaced `~/.cursor/mcp.json` — merge `Guru` into existing `mcpServers`, don't overwrite the whole file |
| Flat formatting in Guru | Paste **section by section** into template fields — bulk-paste flattens heading styles |
| Images missing in Guru draft | Expected — MCP can't upload images. Upload `*-bordered.png` from `examples/<pattern>/images/` manually |
| Duplicate card warning | Skill found a similar card in Guru — check CSKB before publishing a second one |
| Border script fails | Run `pip install pillow`, or border images yourself and skip the script |
| Google Doc won't work | Export to PDF/DOCX or paste content — share links alone aren't readable |

## More detail

- Skill workflow: [SKILL.md](SKILL.md)
- Guru template sections: [guru-template.md](guru-template.md)
- MCP publish config: [guru-config.md](guru-config.md)
- CSKB style guide: [Writing a Knowledge Base Card](https://app.getguru.com/card/TnA5dkRc/Writing-a-Knowledge-Base-Card)
