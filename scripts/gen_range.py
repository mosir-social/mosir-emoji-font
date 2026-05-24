import os
import re
import sys

# Keycap bases that can overmatch regular text if included in unicode-range
KEYCAP_BASES = {0x23, 0x2A, *range(0x30, 0x3A)}  # #, *, 0-9
KEYCAP_MARK = 0x20E3


def parse_codepoints(filename: str):
    name = os.path.splitext(filename)[0]
    parts = re.split(r"[_-]", name)

    cps = []
    for part in parts:
        try:
            cps.append(int(part, 16))
        except ValueError:
            continue
    return cps


def generate_unicode_range(directory: str) -> str:
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    codepoints = set()

    for filename in os.listdir(directory):
        if not filename.endswith(".svg"):
            continue

        cps = parse_codepoints(filename)
        if not cps:
            continue

        # Keep range conservative to avoid overmatching:
        # - Single-codepoint emoji: include directly
        # - Multi-codepoint sequences: include only leading codepoint
        #   (except keycaps, to avoid matching plain #/*/0-9 text)
        if len(cps) == 1:
            codepoints.add(cps[0])
            continue

        first = cps[0]
        if KEYCAP_MARK in cps and first in KEYCAP_BASES:
            continue

        codepoints.add(first)

    if not codepoints:
        raise RuntimeError("No valid emoji codepoints found.")

    sorted_cp = sorted(codepoints)
    ranges = []
    start = prev = sorted_cp[0]

    for cp in sorted_cp[1:]:
        if cp == prev + 1:
            prev = cp
        else:
            ranges.append((start, prev))
            start = prev = cp
    ranges.append((start, prev))

    css_parts = []
    for s, e in ranges:
        css_parts.append(f"U+{s:X}" if s == e else f"U+{s:X}-{e:X}")

    return "unicode-range: " + ", ".join(css_parts) + ";"


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else "build/renamed_svgs"
    try:
        print(generate_unicode_range(directory))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
