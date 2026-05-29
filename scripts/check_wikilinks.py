from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
IGNORED_TOP_LEVEL = {"plans", "templates", "09_ingestion_reports"}


def normalize_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    target = target.replace("\\", "/")
    if "/" in target:
        target = target.rsplit("/", 1)[-1]
    return target.removesuffix(".md")


def main() -> int:
    all_md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    md_files = [
        p
        for p in all_md_files
        if p.relative_to(ROOT).parts[0] not in IGNORED_TOP_LEVEL
    ]
    by_stem: dict[str, list[Path]] = defaultdict(list)
    linked: set[Path] = set()
    broken: list[tuple[Path, str]] = []

    for path in all_md_files:
        by_stem[path.stem].append(path)

    duplicates = {
        stem: paths
        for stem, paths in by_stem.items()
        if len(paths) > 1 and stem != "_README"
    }

    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in WIKILINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if not target:
                continue
            candidates = by_stem.get(target, [])
            if candidates:
                linked.update(candidates)
            else:
                broken.append((path.relative_to(ROOT), match.group(1)))

    important_dirs = {"04_methods", "05_theory", "06_exam_patterns", "07_solved_examples", "08_review"}
    orphan_important = [
        p.relative_to(ROOT)
        for p in md_files
        if p not in linked
        and p.name != "_README.md"
        and p.parts[0] in important_dirs
    ]

    print(f"Markdown files checked: {len(md_files)}")
    print(f"Archival/template files ignored: {len(all_md_files) - len(md_files)}")
    print(f"Broken links: {len(broken)}")
    for source, link in broken[:100]:
        print(f"  BROKEN {source}: [[{link}]]")
    if len(broken) > 100:
        print(f"  ... {len(broken) - 100} more")

    print(f"Duplicate note names: {len(duplicates)}")
    for stem, paths in sorted(duplicates.items()):
        joined = ", ".join(str(p.relative_to(ROOT)) for p in paths)
        print(f"  DUPLICATE {stem}: {joined}")

    print(f"Orphan important notes: {len(orphan_important)}")
    for path in orphan_important[:100]:
        print(f"  ORPHAN {path}")
    if len(orphan_important) > 100:
        print(f"  ... {len(orphan_important) - 100} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
