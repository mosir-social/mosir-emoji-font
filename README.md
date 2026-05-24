# twemoji-mosir

A reusable **Twemoji-based color emoji font package** for the Mosir social platform.

This project wraps the upstream Twemoji SVG assets and builds distributable emoji fonts (COLRv1 + COLRv0), so other projects can reuse the same emoji rendering stack.

## What this repository provides

- Twemoji source as a git submodule (`vendor/twemoji`)
- Build pipeline to generate:
  - `twemoji-mosir.colr_1` (modern COLRv1)
  - `twemoji-mosir.colr_0` (legacy COLRv0)
- Output formats:
  - `.ttf`
  - `.otf`
  - `.woff2`
- Filename normalization + compatibility duplication for better browser/platform support

## Why two color formats?

- **COLRv1**: modern color font format (better gradients/features on modern engines)
- **COLRv0**: fallback for older engines (including Safari/legacy stacks)

Ship both and let CSS/browser selection pick the best available format.

## Prerequisites

- Python 3
- [go-task](https://taskfile.dev/) (`task` command)
- `ninja` (recommended by `nanoemoji`)

## Quick start

```bash
# 1) Get Twemoji submodule
task init

# 2) Create venv + install tooling
task install

# 3) Build all fonts
task
```

Generated font files are placed in `fonts/`.

## Download guide (GitHub)

Just want the font files? Start here 👇

### Quick download (no coding needed)

1. Open the latest release:
   https://github.com/mosir-social/mosir-emoji-font/releases/latest
2. Under **Assets**, download the files you need.
3. Add them to your project.

Which file should you pick?

- **Website** → use `.woff2`
- **Desktop/app use** → use `.ttf` or `.otf`

> Tip: Download from **Assets**. The "Source code (zip)" file is just the repository source, not the ready-to-use font package.

### Want to build fonts yourself? (advanced)

```bash
git clone https://github.com/mosir-social/mosir-emoji-font.git
cd mosir-emoji-font
task init
task install
task
```

Built font files will be generated in `fonts/`.

## Build tasks

- `task init` – initialize Twemoji submodule (shallow)
- `task install` – create `.venv` and install `nanoemoji`, `fonttools`, `brotli`
- `task rename` – normalize SVG names (`-` -> `_`) and generate conservative compatibility duplicates
- `task build-v1` – build COLRv1 TTF/OTF
- `task build-v0` – build COLRv0 TTF/OTF
- `task compress` – generate WOFF2 from built fonts
- `task gen-range` – generate `fonts/unicode_range.css` from prepared SVGs
- `task clean` – remove build artifacts

## Reuse in web projects

If you generate `fonts/unicode_range.css`, you can optionally apply it in your `@font-face`.

Example:

```css
@font-face {
  font-family: "twemoji-mosir";
  src: url("./fonts/twemoji-mosir.colr_1.woff2") format("woff2");
  font-display: swap;
  /* Optional: paste content from fonts/unicode_range.css */
  /* unicode-range: ...; */
}

.emoji-enabled {
  font-family: "twemoji-mosir", "Apple Color Emoji", "Segoe UI Emoji", sans-serif;
}
```

If you target older engines, also serve COLRv0 output as fallback.

Note: `unicode_range.css` intentionally excludes keycap base characters (`#`, `*`, `0-9`) to avoid overmatching normal text.

## Repository structure

- `Taskfile.yml` – main build pipeline
- `scripts/gen_range.py` – unicode-range generator
- `vendor/twemoji/` – upstream Twemoji source (submodule)
- `build/` – temporary build outputs (ignored)
- `fonts/` – distributable font artifacts (committed)

## Attribution & licensing

This project repackages Twemoji artwork. Please keep proper attribution when redistributing.

- Twemoji graphics: **CC-BY 4.0**
- Twemoji code: **MIT**
- Upstream project: https://github.com/jdecked/twemoji

See upstream license files in `vendor/twemoji/LICENSE` and `vendor/twemoji/LICENSE-GRAPHICS` for full terms.

---

If you publish this package, include attribution to Twemoji in your package README and/or NOTICE file.