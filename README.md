# SA Solutions Toolkit

A personal toolkit for SA workflows: generalize customer solutions into reusable assets and browse them in an interactive library.

**Repo:** https://github.com/rebecca-iterable/sa-solutions-toolkit

## Projects

| POC | Folder | Purpose |
|-----|--------|---------|
| Guru card generator | `.cursor/skills/guru-card-generator/` | Turn customer-specific solution docs into generalized Guru cards — [team guide](.cursor/skills/guru-card-generator/README.md) |
| Solutions library | `app/`, `sql/`, `data/` | Searchable catalog of generalized solutions with demo links |

## Clone and open in Cursor

```bash
git clone https://github.com/rebecca-iterable/sa-solutions-toolkit.git
cd sa-solutions-toolkit
```

In Cursor: **File → Open Folder** → select `sa-solutions-toolkit`.

The **guru-card-generator** skill is included at `.cursor/skills/guru-card-generator/`. See the [team guide](.cursor/skills/guru-card-generator/README.md) for Guru MCP setup, prompts, and how to add the skill to another project instead of cloning this repo.

## Quick start (solutions library app)

```bash
cd sa-solutions-toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Folder structure

```
sa-solutions-toolkit/
├── .cursor/skills/guru-card-generator/   # Cursor skill (POC 2)
├── app/                                   # Streamlit app (POC 1)
├── data/solutions/                        # Generalized solution YAML files
├── docs/                                  # Templates and transformation rules
├── scripts/                               # Python utilities
└── sql/                                   # Database schema and queries
```

## Workflow

1. Paste a customer solution doc into Cursor and run the **guru-card-generator** skill.
2. Save the generalized output to `data/solutions/`.
3. Seed the database: `python scripts/seed_db.py`
4. Browse solutions: `streamlit run app/main.py`
