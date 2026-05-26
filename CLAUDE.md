# Laptop Research Project

Research notes for Linux-compatible laptops with sustained CPU performance.

## File Structure
- `laptop-research-summary.md` - Quick reference and recommendations
- `cpu-comparison.md` - CPU benchmarks (AMD, Intel, Qualcomm)
- `reviews/` - Individual laptop review files (with YAML frontmatter, one model per file)
- `overviews/` - Thematic overview articles (platform comparisons, LPCAMM2 guide, excluded models, etc.)
- `laptops.jsonl` - Structured data extracted from review frontmatter
- `scripts/` - Extraction and validation tooling
- `CHANGELOG.md` - Research update log (see Changelog section below)

## Structured Data Pipeline

Each `reviews/*.md` file has YAML frontmatter with structured laptop specs (model, variants, CPU/GPU/RAM, power limits, benchmarks, noise, Linux compat). The Pydantic schema is in `scripts/models.py`.

To extract/validate all frontmatter into `laptops.jsonl`:
```bash
uv run python -m scripts.extract
```

When adding or updating a review:
1. Add/update YAML frontmatter at the top of the markdown file
2. The frontmatter `slug` must match the filename (without `.md`)
3. Run `uv run python -m scripts.extract` to validate and regenerate JSONL
4. Run `uv run -m pytest` to catch stale generated data and broken internal links
5. Commit both the updated `.md` and `laptops.jsonl`

### Frontmatter conventions
- `status`: recommended | available | not_recommended | announced | excluded
- `linux.status`: excellent (OOB, no workarounds) | good (minor issues) | fair (needs custom kernel/boot params) | poor (major breakage) | unknown
- `linux.notes`: positive attributes (e.g. Ubuntu Certified); `linux.issues`: actual problems
- `noise.*_dba`: idle (fans off), low_power (whisper/silent), balanced, performance, max (turbo/stress)
- `power.pl1_w` / `pl2_w`: use float (e.g. 22.5, not 22)
- `variants[].weight_kg` and `variants[].status`: use these when generations differ materially; top-level fields describe the current/default comparison target
- `battery_wh` at variant level when it differs between variants; top-level value is the default/base
- `sources`: list of URLs; move pure-link "Sources" sections from body into frontmatter, keep inline references in text

## Guidelines
- Focus on sustained multi-core performance under Linux
- Include kernel requirements and known issues
- Cite sources (NotebookCheck, Phoronix, linux-hardware.org)
- Track thermal/noise data at different power profiles
- Always include YAML frontmatter in review files (see existing reviews for format)

## Consistency Rules

When modifying any data, ensure it stays consistent across all files that reference it:

### Single source of truth
- **Per-model specs and benchmarks** → `reviews/<slug>.md` frontmatter (authoritative)
- **Structured data** → `laptops.jsonl` (generated, never edit by hand)
- **Summary tables and decision matrix** → `laptop-research-summary.md`
- **README top picks** → `README.md`
- **CPU benchmark table** → `cpu-comparison.md`

### After every data change
1. Update the review file frontmatter first (source of truth)
2. Run `uv run python -m scripts.extract` — must pass with no errors
3. Run `uv run -m pytest` — must pass with generated JSONL current and internal links valid
4. Update `laptop-research-summary.md` tables if the change affects comparison data or recommendations
5. Update `README.md` top picks if recommendations change
6. Update `cpu-comparison.md` if new CPU data is added
7. Update `CHANGELOG.md`
8. Commit updated `.md` files and `laptops.jsonl` together

### File organization
- `reviews/` — one file per model line, NOT per generation. Generations go as `variants` in frontmatter. Example: ThinkPad T14 Gen 5/6/7 → single `lenovo-thinkpad-t14-amd.md`
- `overviews/` — thematic articles (platform comparisons, technology guides, excluded models). No `model:` in frontmatter
- No years or generation numbers in filenames — use slug based on model line name
- Framework 13 (old) and Framework 13 Pro are separate products → separate files

### Data accuracy
- `power.pl1_w` / `pl2_w` must be actual measured sustained/burst values from reviews, NOT cTDP spec ranges from AMD/Intel datasheets
- If sustained power is not yet reviewed, use conservative estimates and note "est." in body text
- Benchmark scores must cite the specific review source — same CPU in different laptops gives different scores
- RAM details matter: always record `ram_type` (LPDDR5X, DDR5 SO-DIMM, LPCAMM2 — these are not interchangeable), speed grade when known (e.g. DDR5-5600, LPDDR5X-7500), and max capacity. Specify per-variant when Intel/AMD variants differ (e.g. Framework 13 Pro). `ram_upgradeable` is a secondary detail — RAM type, speed, and max capacity are more important for comparison
- Do not reuse workstation CPU ceilings for mainstream lines with similar chassis names. Example: ThinkPad P14s Gen 7 AMD has HX PRO 470; ThinkPad T14/T14s Gen 7 AMD top out at Ryzen AI 7 PRO 450.
- Prices: specify currency. `price_usd` in frontmatter is USD; note EUR/other in body text

### When adding new models
- Search for existing file for the same model line before creating a new one — add as a variant
- Status `announced` for unreviewed models; change to `available`/`recommended` when sustained power data is confirmed by independent review
- Don't claim sustained power numbers without a review source — laptop thermal design varies wildly for the same CPU

## Changelog
Maintain `CHANGELOG.md` in the project root. Update it with every commit that changes research content.

Format — reverse-chronological, grouped by date:
```
## YYYY-MM-DD

### Added
- New model: <Model Name> — <one-line summary with key specs>

### Updated
- <Model Name> — <what changed: new benchmark data, revised sustained power, etc.>

### Removed / Excluded
- <Model Name> — <reason: throttling confirmed, discontinued, etc.>

### Recommendations
- <Any changes to top picks or decision matrix>
```

Rules:
- One entry per date, combine multiple changes under the same date
- Only log substantive research changes (new models, updated data, changed recommendations)
- Don't log formatting-only or typo-fix commits
- Reference sources when adding new data
