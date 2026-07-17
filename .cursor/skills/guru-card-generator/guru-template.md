# Guru Knowledge Base Card Template

Canonical source: [Customer Solutions Knowledge Base](https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base) collection in Guru.

Style guide: [Writing a Knowledge Base Card](https://app.getguru.com/card/TnA5dkRc/Writing-a-Knowledge-Base-Card)

**Publish to:** Customer Solutions Knowledge Base collection.

Use this structure when converting **any** customer solutions doc into a Guru card. Adapt each section to the Iterable features in the source — Journeys, campaigns, catalogs, data feeds, webhooks, etc.

---

## Card title

**Format:** `[Pattern name]: [Iterable capability] + [Integration/partner]`

Examples (across different SA patterns):
- Real-time Experiment Assignment: Journey Live Data + Statsig
- Cart Abandonment Recovery: Event-triggered Journey + Segment
- Product Recommendations in Email: Catalog + Data Feeds
- Order Confirmation SMS: Triggered Campaign + Shopify
- Audience Sync for Paid Media: Lists + Reverse ETL

Write for search — include Iterable feature names and the use case, not the customer name.

---

## Purpose

What this pattern does, when to recommend it, and prerequisites. Combine what might be split across "overview" and "use case" in a solutions doc into this single section.

Include:
- 1–2 sentences on what the pattern does and the primary outcome
- **When to recommend** — bullet triggers ("Recommend when a customer…")
- **Iterable prerequisites** — features/plan required for this pattern

> A reader should know in 10 seconds whether this card applies to their deal.

---

## Problem

The business or technical pain point, in general terms:
- What breaks with the status-quo approach
- Why the current workflow fails
- Impact on messaging, personalization, measurement, or operations

Do **not** include customer names, account IDs, or deal-specific metrics.

---

## Solution

High-level approach in 2–4 sentences, followed by bullet benefits:
- Which Iterable feature(s) solve the problem
- What the customer no longer needs to do

---

## Architecture

How the pieces connect. Include when the doc describes a data flow or system integration:
- A **mermaid flowchart** (adapt nodes to the actual features — journey tiles, campaign trigger, catalog API, webhook, warehouse, etc.)
- Setup order when features depend on each other
- Real-time vs. batch, where relevant

Apply product constraints **only when they apply to this pattern** (e.g., journey branching vs. campaign limitations).

For Guru: export the Mermaid diagram as PNG (see below) and upload in the card editor — Guru does not render Mermaid.

---

## Iterable components *(optional)*

Include only when the solution uses many features and a quick scannable list helps. **Skip** if Architecture and Implementation already cover the same ground.

---

## Integrations *(optional)*

Include only when multiple third-party systems play distinct roles. **Skip** for simple two-system patterns (e.g., Iterable + one partner) where Architecture already explains the relationship. Use a table only when there are 3+ integrations with different responsibilities.

---

## Implementation

Numbered setup steps from the solutions doc:
- Iterable UI navigation paths
- API endpoints, headers, payload shapes
- Config values that must match across systems

Replace customer-specific values with placeholders: `YOUR-SECRET-KEY`, `your_resource_name`, `{{userId}}`.

---

## Testing

How to validate the solution works — match the doc's testing approach:
- Journey test mode, campaign proof send, API test call, catalog preview, etc.
- Expected responses or UI outcomes

---

## Example setup

**Optional.** Include only when the source doc has UI walkthrough content (screenshots, click-by-click setup).

Use a feature-specific subtitle:
- "Example journey" — journey canvas screenshots
- "Example campaign" — campaign editor screenshots
- "Example catalog sync" — catalog or data feed config
- etc.

**If UI walkthrough exists but screenshots are missing:** ask the user to upload in chat. Save to `examples/<pattern-slug>/images/`, run [scripts/add-image-borders.py](scripts/add-image-borders.py), and embed bordered files:

```bash
python .cursor/skills/guru-card-generator/scripts/add-image-borders.py examples/<pattern-slug>/images/
```

```markdown
### Example campaign
![Campaign audience configuration](images/campaign-audience-bordered.png)
```

When publishing to Guru, upload the `*-bordered.png` files in the card editor (markdown links are not imported on paste).

### Screenshot redaction (required before publish)

Screenshots often expose secrets that text placeholders already hide. **Redact or crop before uploading to Guru:**

| Often exposed in screenshots | Action |
|------------------------------|--------|
| API keys, server secrets (`secret-...`) | Blur or replace with `YOUR-SECRET-KEY` |
| Webhook auth headers / custom header values | Redact value column |
| Project or account names in UI chrome | Crop or blur |
| Real `userId` / email in test panels | Use generic test values |

Webhook and integration config screenshots are the highest risk — always review custom headers and credential fields.

Internal repo copies in `examples/` may retain originals for SA reference; **published Guru cards use redacted `*-bordered.png` files only**.

**Image borders (required):** Guru does not add borders. After saving or receiving screenshots, always run `scripts/add-image-borders.py` on the images folder and reference `*-bordered.png` in the card markdown.

---

## Gotchas and limitations

From the source doc — common mistakes, edge cases, when this pattern is **not** the right fit.

Do not import gotchas from unrelated reference examples.

---

## Related resources

- Iterable product docs (relevant to this pattern)
- Partner/integration docs
- Internal demo assets
- Related Guru cards — link only if the card exists; do not invent placeholder "related" entries

---

## Suggested tags

Comma-separated tags reflecting **this** solution's features and integrations.

---

## Publishing checklist

**Do not bulk-paste markdown into Guru** — heading styles and colors come from the Guru card template, not the markdown file.

1. Create a new card **from the Customer Solutions Knowledge Base template**
2. Paste each section's **content** into the matching template field (Purpose, Problem, Solution, etc.)
3. Confirm template heading styles in the Guru editor
4. Upload screenshots separately; redact secrets first

Before publishing:

- [ ] No customer or company names
- [ ] No internal contacts, account IDs, or project codenames
- [ ] Specific metrics replaced with qualitative outcomes
- [ ] Placeholders used for secrets and IDs in text
- [ ] **Screenshots redacted** and bordered (`*-bordered.png` used in card)
- [ ] Title and components match the actual Iterable features in the doc
- [ ] Published to **Customer Solutions Knowledge Base** collection
- [ ] Verifier assigned and verification interval set
