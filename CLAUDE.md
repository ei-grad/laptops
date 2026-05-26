# Laptop Research Project

Research notes for Linux-compatible laptops with sustained CPU performance.

## File Structure
- `laptop-research-summary.md` - Quick reference and recommendations
- `laptop-detailed-reviews.md` - Full review data per model
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
4. Commit both the updated `.md` and `laptops.jsonl`

### Frontmatter conventions
- `status`: recommended | available | not_recommended | announced | excluded
- `linux.status`: excellent (OOB, no workarounds) | good (minor issues) | fair (needs custom kernel/boot params) | poor (major breakage) | unknown
- `linux.notes`: positive attributes (e.g. Ubuntu Certified); `linux.issues`: actual problems
- `noise.*_dba`: idle (fans off), low_power (whisper/silent), balanced, performance, max (turbo/stress)
- `power.pl1_w` / `pl2_w`: use float (e.g. 22.5, not 22)
- `battery_wh` at variant level when it differs between variants; top-level value is the default/base
- `sources`: list of URLs; move pure-link "Sources" sections from body into frontmatter, keep inline references in text

## Guidelines
- Focus on sustained multi-core performance under Linux
- Include kernel requirements and known issues
- Cite sources (NotebookCheck, Phoronix, linux-hardware.org)
- Track thermal/noise data at different power profiles
- Always include YAML frontmatter in review files (see existing reviews for format)

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
