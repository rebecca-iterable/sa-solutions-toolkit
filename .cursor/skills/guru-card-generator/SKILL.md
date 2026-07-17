---
name: guru-card-generator
description: >-
  Transform a customer-specific solutions doc into a generalized Guru card draft
  and create a Guru draft via MCP when connected. Works for any Iterable feature.
  Use when the user pastes or uploads a solution doc, links a Google Doc export,
  or asks to generalize customer info for the Customer Solutions Knowledge Base.
---

# Guru Card Generator

Convert a customer-specific solutions document into a generalized Guru card ready to paste into Guru.

**Template:** [guru-template.md](guru-template.md) → publish to [Customer Solutions Knowledge Base](https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base)

**Reference examples:** [examples/README.md](examples/README.md) — one before/after per pattern. The Statsig / Journey Live Data example is illustrative, not prescriptive.

## When to use

- User pastes, uploads, or references a solutions doc (PDF, markdown, Google Doc export)
- User asks to "generalize", "anonymize", "create a Guru card", or "post to Guru"
- User wants to remove customer-specific details for the Customer Solutions Knowledge Base

**Google Docs:** A share link alone is not readable — ask the user to export (PDF/DOCX), paste the doc content, or upload the file to Cursor.

## Input sources

| Source | Action |
|--------|--------|
| PDF / file upload | Read the file |
| Pasted text / markdown | Use directly |
| Local path in repo | Read file |
| Google Doc URL only | Ask user to export or paste — do not pretend to fetch the doc |
| Google Doc PDF/DOCX export | Read exported file |

## Workflow

### 1. Read the input and identify Iterable features

Read the solutions doc and determine which **Iterable capabilities** it covers. Do not assume Journeys — derive features from the source.

**Common feature areas** (use only what appears in the doc):

| Area | Examples |
|------|----------|
| **Journeys** | Tiles (Live Data, Message, Attribute split, Filter, Delay), Journey Webhooks |
| **Campaigns** | Blast, triggered, A/B experiments, send schedules |
| **Messaging** | Email, SMS, push, in-app, WhatsApp templates |
| **Data & audiences** | Lists, segments, user fields, catalog, data feeds, reverse ETL |
| **Integrations** | System webhooks, Journey Webhooks, API (users, events, catalog) |
| **Personalization** | Handlebars, snippets, data feeds, dynamic content |
| **Experimentation** | Iterable experiments, holdout groups, external tools (Statsig, Optimizely) |

Extract content into Guru sections:

| Solutions doc section | Guru card section |
|-----------------------|-------------------|
| Purpose / Title | Card title + **Purpose** |
| Customer context / when to recommend | **Purpose** (under "When to recommend") |
| Context / Problem | **Problem** |
| Solution | Solution |
| Architecture / diagram | Architecture (+ export Mermaid as PNG for Guru) |
| Iterable components | *(optional)* — only if not redundant with Architecture |
| Integrations / partners | *(optional)* — only for multi-system patterns |
| Setup / Implementation | Implementation |
| Test | Testing |
| Lessons learned / edge cases | Gotchas and limitations |
| UI walkthrough / screenshots | Example setup (feature-specific subtitle) |
| Demo links | Related resources |

If the source doc lacks a section, infer it from context or omit.

**Title format:** `[Pattern name]: [Iterable capability] + [Integration/partner if any]`

Examples across the SA team:
- Real-time Experiment Assignment: Journey Live Data + Statsig
- Catalog-Based Product Recommendations: Data Feeds + Shopify
- Post-Purchase Cross-Sell: Triggered Campaign + Segment

### 1b. Collect screenshots (only when UI walkthrough content is detected)

**Ask the user to upload screenshots only if** the source doc contains UI walkthrough signals **and** images are not already attached or extractable.

**Detection signals** — ask for uploads when the doc includes any of:
- Screenshot images or "(Screenshot)" / image placeholders
- Sections like "Setup", "Configuration", "Example journey/campaign", or step-by-step Iterable UI navigation
- Language like "click", "select", "as shown below", "see image", or numbered UI steps with screen references

**Do not ask** when the doc is purely conceptual (problem/solution/architecture prose with no UI walkthrough).

When triggered:
1. **Ask the user** to upload screenshots relevant to *this* solution (journey canvas, campaign editor, catalog mapping, webhook config, etc.)
2. Save originals to `examples/<pattern-slug>/images/` with descriptive filenames
3. **Add borders to all images** — run `python scripts/add-image-borders.py examples/<pattern-slug>/images/` (creates `*-bordered.png` for each PNG)
4. Embed **bordered** images in **Example setup** (`images/name-bordered.png`) — Guru does not add borders in the editor
5. Redact secrets in originals before or during border step; publish bordered copies only

Also border exported diagrams (e.g., Mermaid PNGs) with the same script.

If UI walkthrough content exists but the user declines, include **Example setup** with text only.

If there is no UI walkthrough content, omit **Example setup** entirely.

### 2. Anonymize

| Remove | Replace with |
|--------|--------------|
| Customer/company names | Industry label ("retail brand") or omit |
| Account IDs, project codenames | Omit |
| Internal contacts (CSM, SA names) | Omit |
| Specific lift metrics ("12% increase") | Qualitative outcome ("improved engagement") |
| Real API keys, secrets | `YOUR-SECRET-KEY` |
| Customer-specific resource names | Generic placeholders (`your_experiment_id`, `your_catalog_name`) |
| Real IDs from test responses | `<id>` placeholders |

Keep technical accuracy — endpoints, header names, payload shapes, and Iterable UI paths from the source doc should stay exact.

### 3. Apply product accuracy (from the source doc only)

Validate claims against what the **source doc actually describes**. Do not copy rules from one reference example into unrelated cards.

**Universal checks:**
- Data warehouse sync direction is **warehouse → Iterable** when batch sync is discussed
- Screenshots: ask only when UI walkthrough content is detected and images are missing

**Apply only when relevant to this doc** — examples:
- Journeys branch; campaigns do not (experiment routing patterns)
- Journey Webhook before Live Data tile (Live Data patterns)
- Attribute split vs. filter yes/no for branching — filter yes/no chains on Live Data fields (Control filter → Test on no path → exit); Statsig uses JSON key `userID` with Iterable `{{userId}}`
- Catalog field mapping before template personalization (catalog patterns)

If unsure about Iterable product behavior, state what the solutions doc shows and flag for SA review rather than inventing constraints.

### 4. Generalize

Reframe deal-specific language as reusable guidance:

- "This customer wanted…" → "Recommend when a customer…"
- "We built them…" → pattern description any SA can recommend
- Deal outcomes → qualitative benefits

### 5. Map to Guru format

Follow [guru-template.md](guru-template.md). **Use the Guru template's exact section headings** (e.g., **Purpose**, **Problem** — not Overview or Use case). Output markdown with `##` headings that match the Customer Solutions Knowledge Base card template.

### 6. Quality check

- [ ] No customer names, account IDs, or internal contacts
- [ ] Secrets and IDs use placeholders in text
- [ ] **Screenshots redacted** before border step; embedded markdown uses `*-bordered.png` files
- [ ] Title reflects the actual Iterable features in the doc (not a generic journey title)
- [ ] Iterable components / Integrations omitted when redundant with Architecture
- [ ] Implementation steps are copy-pasteable with placeholder substitution
- [ ] Gotchas come from the source doc, not from unrelated examples
- [ ] Example setup included only when source has UI walkthrough content
- [ ] Card targets **Customer Solutions Knowledge Base** collection

### 7. Optional — solutions library YAML

If the user wants to save to `data/solutions/`:

```yaml
title: "<from card title>"
use_case: "<one line>"
problem: "<one line>"
architecture: "<data flow summary>"
iterable_components: "<comma-separated, from doc>"
integrations: "<partners/tools>"
demo_url: ""
guru_card_path: ""
tags: "<relevant tags from doc>"
```

### 8. Create Guru draft via MCP (default when connected)

When **Guru MCP** (`user-Guru`) is available, create a draft after steps 1–6 unless the user opts out.

Config: [guru-config.md](guru-config.md)

**Workflow:**

1. `guru_search_documents` — search for similar titles; warn if duplicate exists
   - `agentId`: `51f0df10-e60f-41d1-a1eb-8976889fd7dd`
2. Build card `content` from generated markdown (body only — no `#` title line, no internal repo notes, no Tags section)
3. `guru_create_draft`:
   - `title`: `WIP: {searchable card title}`
   - `content`: full card body
4. Save local files:
   - `examples/<pattern-slug>/output-guru-card.md`
   - `examples/<pattern-slug>/images/*` (bordered screenshots if any)
5. Return to user:
   - Draft created confirmation (link/ID from MCP response)
   - **Manual steps in Guru** (MCP cannot do these):
     - Open draft → select **Customer Solutions Knowledge Base** collection
     - Choose folder
     - Paste content into template sections if styles are missing
     - Upload `*-bordered.png` images
     - Add tags, verifier → publish (remove `WIP` from title)

**MCP cannot:** set collection/folder, upload images, apply template colors, or publish.

**Prompt example:**
> "Generalize this solutions doc and create a Guru draft in CSKB."

## Output format

1. **Guru card** — local markdown (`examples/<pattern>/output-guru-card.md`)
2. **Guru draft** — created via MCP when connected (link + manual follow-up checklist)
3. **Changes made** — brief bullets (only if non-obvious)

## Reference example

The [statsig-journey-live-data](examples/statsig-journey-live-data/) example shows transformation quality for one Journey pattern. Use it for tone and structure, not as the feature list for every card.

| Before (solutions doc) | After (Guru card) |
|------------------------|-------------------|
| "Purpose: To assign and retrieve…" | **Purpose** section (what + when to recommend) |
| Customer context / use case bullets | **Purpose** → "When to recommend" |
| Context / stale assignment pain | **Problem** |
| Customer-specific resource names | Generic placeholders |
| "Campaigns or journeys branch" | Correct per feature (only if doc discusses branching) |
| UI screenshots | **Example setup** only when walkthrough detected |
| No gotchas section | **Gotchas** from source doc failure modes |
| Text-only architecture | Mermaid flowchart when data flow exists |

## Additional resources

- Team template: [guru-template.md](guru-template.md)
- Examples index: [examples/README.md](examples/README.md)
- Statsig reference: [examples/statsig-journey-live-data/](examples/statsig-journey-live-data/)
- Solutions doc input format: [docs/solution-template.md](../../../docs/solution-template.md)
- Border script: [scripts/add-image-borders.py](scripts/add-image-borders.py)
- Guru MCP config: [guru-config.md](guru-config.md)
