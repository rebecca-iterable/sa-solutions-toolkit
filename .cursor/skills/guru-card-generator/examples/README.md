# Guru card examples

Each subfolder is one **reference transformation** — a before/after pair for a specific Iterable pattern. Use these to calibrate output quality, not as the only valid card structure.

| Example | Iterable features | Integration |
|---------|-------------------|-------------|
| [statsig-journey-live-data](statsig-journey-live-data/) | Journey Webhooks, Live Data, Attribute split | Statsig |

Add new examples as the team documents more patterns:

```
examples/
  your-pattern-name/
    input-solution-doc.md
    output-guru-card.md
    images/          # originals + *-bordered.png (use bordered for Guru)
```

When adding an example, keep feature-specific product rules in that example's output — not in `SKILL.md`.
