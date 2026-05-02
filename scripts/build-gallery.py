#!/usr/bin/env python3
"""Scan the repo for .drawio files and rewrite the FILES list inside index.html."""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "index.html"
START = "<!-- FILES:START -->"
END = "<!-- FILES:END -->"

EXCLUDE_TOP_DIRS = {".git", "scripts", "Others"}
SUBGROUP_DIRS = {"Term1", "Term2", "Term 1", "Term 2", "SummerCourse", "Cyber", "Modeling"}


def is_backup(name: str) -> bool:
    return name.startswith(".$") or name.endswith(".bkp")


def collect() -> list[dict]:
    files: list[dict] = []
    for top in sorted(p for p in REPO_ROOT.iterdir() if p.is_dir() and p.name not in EXCLUDE_TOP_DIRS):
        for dirpath, dirnames, filenames in os.walk(top):
            dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
            rel_dir = Path(dirpath).relative_to(REPO_ROOT)
            parts = rel_dir.parts
            if len(parts) >= 2 and parts[1] in SUBGROUP_DIRS:
                group = f"{parts[0]} / {parts[1]}"
            else:
                group = parts[0]
            for fname in sorted(filenames):
                if not fname.endswith(".drawio"):
                    continue
                if is_backup(fname):
                    continue
                rel = (rel_dir / fname).as_posix()
                files.append({
                    "path": rel,
                    "name": fname[:-len(".drawio")],
                    "group": group,
                })
    files.sort(key=lambda f: (f["group"], f["name"].lower()))
    return files


def rewrite(files: list[dict]) -> None:
    html = INDEX_HTML.read_text(encoding="utf-8")
    if START not in html or END not in html:
        sys.exit(f"Sentinels {START!r} / {END!r} not found in {INDEX_HTML}")
    payload = json.dumps(files, indent=2, ensure_ascii=False)
    block = f"{START}\nconst FILES = {payload};\n{END}"
    new_html = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _m: block,
        html,
        count=1,
        flags=re.DOTALL,
    )
    INDEX_HTML.write_text(new_html, encoding="utf-8")


def main() -> None:
    files = collect()
    rewrite(files)
    groups = {f["group"] for f in files}
    print(f"Wrote {len(files)} files across {len(groups)} groups.")


if __name__ == "__main__":
    main()
