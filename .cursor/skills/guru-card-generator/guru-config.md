# Guru MCP publish config

Use when calling `guru_create_draft` after generating a card.

## Target collection

| Field | Value |
|-------|-------|
| Name | Customer Solutions Knowledge Base (CSKB) |
| URL | https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base |
| Board (drafts) | https://app.getguru.com/boards/T4baKBRc/In-Draft |

## Template

Create cards from **Knowledge Base General Card Template** in Guru UI (see [Writing a Knowledge Base Card](https://app.getguru.com/card/TnA5dkRc/Writing-a-Knowledge-Base-Card)).

Section headings in generated content must match the template:

- **Purpose** (not Overview)
- **Problem**
- Solution, Architecture, Implementation, Testing, Example setup, Gotchas and limitations, Related resources

## MCP settings

| Field | Value |
|-------|-------|
| MCP server | `user-Guru` |
| Search/create draft tool | `guru_search_documents`, `guru_create_draft` |
| Knowledge agent ID | `51f0df10-e60f-41d1-a1eb-8976889fd7dd` (Guru) |

## Draft title

Prefix with `WIP: ` while drafting (per CSKB guide). Remove `WIP` before publish.

Example: `WIP: Real-time Experiment Assignment: Journey Live Data + Statsig`

## MCP limitations (manual steps after draft)

`guru_create_draft` accepts only `title` and `content`. It does **not**:

- Assign collection or folder (select **Customer Solutions Knowledge Base** on publish)
- Apply template heading colors/styles (paste into template sections in Guru, or restyle after)
- Upload images (upload `*-bordered.png` files manually)
- Set tags or verifier (on publish workflow)

## After `guru_create_draft`

Tell the user to open the draft in Guru and:

1. Confirm collection = **Customer Solutions Knowledge Base**
2. Choose the correct folder
3. Upload bordered screenshots from `examples/<pattern>/images/*-bordered.png`
4. Upload architecture flowchart PNG if present
5. Add tags (max 4 per CSKB guide)
6. Set verifier and publish (remove `WIP` from title)
