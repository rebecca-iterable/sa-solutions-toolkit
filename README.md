# Guru Card Generator

Cursor skill for SAs to turn customer-specific solution docs into generalized [Customer Solutions Knowledge Base (CSKB)](https://app.getguru.com/collections/a9n8p/Customer-Solutions-Knowledge-Base) cards.

**Repo:** https://github.com/rebecca-iterable/sa-solutions-toolkit

## Quick start

```bash
git clone https://github.com/rebecca-iterable/sa-solutions-toolkit.git
cd sa-solutions-toolkit
```

In Cursor: **File → Open Folder** → select `sa-solutions-toolkit`.

Connect [Guru MCP](https://mcp.api.getguru.com/mcp), then prompt:

> *"Generalize this solutions doc and create a Guru draft in CSKB."*

**Full team guide:** [.cursor/skills/guru-card-generator/README.md](.cursor/skills/guru-card-generator/README.md)

## What's included

```
sa-solutions-toolkit/
├── .cursor/
│   ├── rules/guru-card-auto-draft.mdc      # Auto-draft rule when Guru MCP is connected
│   └── skills/guru-card-generator/         # Skill, template, examples, border script
│       ├── SKILL.md
│       ├── README.md                       # Team setup, prompts, troubleshooting
│       ├── guru-template.md
│       ├── guru-config.md
│       ├── docs/solution-template.md       # Input template for new solution docs
│       ├── scripts/add-image-borders.py
│       └── examples/                         # Reference before/after transformations
└── README.md
```

## What it does

- Anonymizes customer-specific details
- Maps content to CSKB Guru template sections
- Saves and borders screenshots for upload
- Creates a `WIP:` draft in Guru via MCP (when connected)

You finish in Guru: CSKB collection, folder, images, tags, verifier, publish.

## Install options

| Method | When to use |
|--------|-------------|
| **Clone this repo** | Recommended — skill + examples + updates via `git pull` |
| **Copy skill folder** | Add `.cursor/skills/guru-card-generator/` to another project |
| **Personal skill** | Copy to `~/.cursor/skills/guru-card-generator/` for use in any project |

See the [team guide](.cursor/skills/guru-card-generator/README.md) for detailed install steps, prompts, and troubleshooting.

## Reference example

[statsig-journey-live-data](.cursor/skills/guru-card-generator/examples/statsig-journey-live-data/) — Journey Live Data + Statsig experiment assignment pattern.
