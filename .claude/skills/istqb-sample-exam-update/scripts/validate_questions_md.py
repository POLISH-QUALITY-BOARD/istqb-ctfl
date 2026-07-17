#!/usr/bin/env python3
"""Validate a questions-<letter>-pl.md file with the *real* upstream parser.

This does not reimplement or approximate the istqb_product_base markdown
schema -- it downloads the actual `_read_md_questions` function from
istqborg/istqb_product_base and runs it against the file, so a pass here
means the CI build will actually parse the file the same way.

Usage:
    python3 validate_questions_md.py <path-to-questions-X-pl.md> [--min N] [--max N]

Exit code is non-zero if parsing fails or any structural check fails.
Prints a (number, learning-objective, k-level, correct) table on success so
it can be eyeballed against the PDF's "Klucz odpowiedzi" table.
"""
import argparse
import importlib.util
import sys
import urllib.request
from pathlib import Path

TEMPLATE_URL = "https://raw.githubusercontent.com/istqborg/istqb_product_base/main/template.py"
CACHE_PATH = Path(__file__).parent / "_template_cache.py"


def _load_template_module():
    if not CACHE_PATH.exists():
        print(f"Downloading {TEMPLATE_URL} -> {CACHE_PATH}", file=sys.stderr)
        urllib.request.urlretrieve(TEMPLATE_URL, CACHE_PATH)
    spec = importlib.util.spec_from_file_location("istqb_template", CACHE_PATH)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ModuleNotFoundError as e:
        missing = str(e).split("'")[1] if "'" in str(e) else str(e)
        print(
            f"Missing dependency '{missing}'. Try: python3 -m pip install --user pyyaml yamale",
            file=sys.stderr,
        )
        raise
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("md_path", type=Path, help="Path to questions-<letter>-pl.md")
    parser.add_argument("--min", type=int, default=1, help="Expected minimum question count")
    parser.add_argument("--max", type=int, default=None, help="Expected exact/maximum question count")
    args = parser.parse_args()

    if not args.md_path.exists():
        print(f"File not found: {args.md_path}", file=sys.stderr)
        sys.exit(1)

    tpl = _load_template_module()

    try:
        results = list(tpl._read_md_questions([args.md_path]))
    except Exception as e:
        print(f"PARSE ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsed {len(results)} questions OK")

    errors = []
    by_num = {}
    for num, q in results:
        if num in by_num:
            errors.append(f"#{num}: duplicate question number")
        by_num[num] = q
        for field in ("learning-objective", "k-level", "question", "answers", "explanation"):
            if field not in q or not q[field]:
                errors.append(f"#{num}: missing or empty '{field}'")
        correct = q.get("correct") or []
        if not correct:
            errors.append(f"#{num}: missing 'correct'")
        answers = q.get("answers") or {}
        for c in correct:
            if c not in answers:
                errors.append(f"#{num}: correct letter '{c}' not among answers {sorted(answers)}")

    if len(results) < args.min:
        errors.append(f"expected at least {args.min} questions, got {len(results)}")
    if args.max is not None and len(results) > args.max:
        errors.append(f"expected at most {args.max} questions, got {len(results)}")

    if errors:
        print("\nSTRUCTURAL ERRORS:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    print("\nAll structural checks passed. Cross-check this against the PDF's own")
    print("\"Klucz odpowiedzi\" table -- letters and LO/K-level should match exactly.\n")
    print(f"{'#':>4}  {'LO':<12} {'K':<4} correct")
    for n in sorted(by_num):
        q = by_num[n]
        print(f"{n:>4}  {q['learning-objective']:<12} {q['k-level']:<4} {','.join(q['correct'])}")


if __name__ == "__main__":
    main()
