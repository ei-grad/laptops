from __future__ import annotations

import re
from pathlib import Path

from scripts.extract import extract_all, write_jsonl

ROOT = Path(__file__).resolve().parents[1]


def test_generated_jsonl_is_current(tmp_path: Path) -> None:
    output = tmp_path / "laptops.jsonl"

    laptops = extract_all()
    write_jsonl(laptops, output)

    assert len(laptops) == len(list((ROOT / "reviews").glob("*.md")))
    assert output.read_text() == (ROOT / "laptops.jsonl").read_text()


def test_repo_relative_markdown_links_exist() -> None:
    markdown_files = [
        *ROOT.glob("*.md"),
        *ROOT.glob("reviews/*.md"),
        *ROOT.glob("overviews/*.md"),
    ]
    markdown_link = re.compile(r"\[[^\]]*]\(([^)#]+)(?:#[^)]+)?\)")
    inline_path = re.compile(r"`([^`]+/[^`]+\.md)`")

    missing: list[str] = []
    for file_path in markdown_files:
        text = file_path.read_text()
        candidates = [match.group(1).strip() for match in markdown_link.finditer(text)]
        candidates.extend(
            match.group(1).strip() for match in inline_path.finditer(text)
        )

        for target in candidates:
            if (
                "://" in target
                or target.startswith("#")
                or "*" in target
                or "<" in target
            ):
                continue

            resolved = (
                (file_path.parent / target)
                if target.startswith(".")
                else (ROOT / target)
            )
            if not resolved.exists():
                rel_path = file_path.relative_to(ROOT)
                missing.append(f"{rel_path}: {target}")

    assert missing == []
