#!/usr/bin/env python3
"""Extract structured laptop data from review frontmatter into JSONL."""

import json
import sys
from pathlib import Path

import frontmatter
from pydantic import ValidationError

from .models import Laptop

REVIEWS_DIR = Path(__file__).parent.parent / "reviews"
OUTPUT_FILE = Path(__file__).parent.parent / "laptops.jsonl"


def extract_all() -> list[tuple[Laptop, Path]]:
    laptops = []
    errors = []

    for md_file in sorted(REVIEWS_DIR.glob("*.md")):
        post = frontmatter.load(md_file)
        if not post.metadata:
            continue

        if "model" not in post.metadata:
            keys = ", ".join(post.metadata.keys())
            print(
                f"  warning: {md_file.name} has frontmatter ({keys}) but no 'model' key, skipping",
                file=sys.stderr,
            )
            continue

        try:
            laptop = Laptop(**post.metadata)
        except ValidationError as e:
            errors.append((md_file.name, e))
            continue

        expected_slug = md_file.stem
        if laptop.slug != expected_slug:
            errors.append(
                (
                    md_file.name,
                    ValueError(
                        f"slug mismatch: frontmatter has '{laptop.slug}', "
                        f"expected '{expected_slug}' (from filename)"
                    ),
                )
            )
            continue

        laptops.append((laptop, md_file))

    if errors:
        print(f"Validation errors in {len(errors)} file(s):", file=sys.stderr)
        for filename, error in errors:
            print(f"\n  {filename}:", file=sys.stderr)
            if isinstance(error, ValidationError):
                for err in error.errors():
                    loc = " -> ".join(str(x) for x in err["loc"])
                    print(f"    {loc}: {err['msg']}", file=sys.stderr)
            else:
                print(f"    {error}", file=sys.stderr)
        sys.exit(1)

    return laptops


REPO_URL = "https://github.com/ei-grad/laptops/blob/main"


def write_jsonl(laptops: list[tuple[Laptop, Path]], output: Path) -> None:
    with output.open("w") as f:
        for laptop, md_file in laptops:
            data = laptop.model_dump(mode="json")
            data["review_url"] = f"{REPO_URL}/reviews/{md_file.name}"
            f.write(json.dumps(data, ensure_ascii=False) + "\n")


def main() -> None:
    laptops = extract_all()
    write_jsonl(laptops, OUTPUT_FILE)
    print(f"Extracted {len(laptops)} laptops to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
