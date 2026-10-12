#!/usr/bin/env python3
"""
Rename files like "notched_Beautiful.mp3" -> "Beautiful-N.mp3".

Usage:
    python rename_notched.py            # runs in the current folder
    python rename_notched.py /path/dir  # runs in another folder
    python rename_notched.py --dry-run  # preview without renaming
"""
import sys
from pathlib import Path

PREFIX = "notched_"
SUFFIX = "-N"


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv
    folder = Path(args[0]) if args else Path.cwd()

    count = 0
    for f in sorted(folder.glob(f"{PREFIX}*.mp3")):
        new_name = f"{f.stem[len(PREFIX):]}{SUFFIX}{f.suffix}"
        target = f.with_name(new_name)
        if target.exists():
            print(f"Skipped (already exists): {new_name}")
            continue
        print(f"{f.name}  ->  {new_name}")
        if not dry_run:
            f.rename(target)
        count += 1

    action = "Would rename" if dry_run else "Renamed"
    print(f"\n{action} {count} file(s).")


if __name__ == "__main__":
    main()
