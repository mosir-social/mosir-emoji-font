# mosir-emoji-font

A simple **re-package of Twemoji** as ready-to-use emoji font files.

> This project does **not** create a new emoji design.
> We package upstream [Twemoji](https://github.com/jdecked/twemoji) into common font formats so it is easy to use in Mosir and other apps.

## Download fonts (recommended)

If you just want to use the fonts, download from Releases:

👉 https://github.com/mosir-social/mosir-emoji-font/releases/latest

From **Assets**, choose files based on your use case:

- **Web**: `.woff2`
- **App/Desktop**: `.ttf` or `.otf`

## What files are included?

Each release includes two compatibility variants:

- `twemoji-mosir.colr_1.*` → modern color font (COLRv1)
- `twemoji-mosir.colr_0.*` → fallback for older engines (COLRv0)

If you are unsure, use COLRv1 first and keep COLRv0 as fallback.

## Basic web usage

```css
@font-face {
  font-family: "twemoji-mosir";
  src: url("./twemoji-mosir.colr_1.woff2") format("woff2");
  font-display: swap;
}

.emoji {
  font-family: "twemoji-mosir", "Apple Color Emoji", "Segoe UI Emoji", sans-serif;
}
```

> Safari/WebKit note: there is a known bug where COLRv0 font painting can leak outside expected bounds.
> If you see this issue, wrap emoji elements with `contain: paint`.

```css
.emoji {
  contain: paint;
}
```

## Attribution & license

This repository repackages Twemoji artwork and metadata.

- Twemoji graphics: **CC-BY 4.0**
- Twemoji code: **MIT**
- Upstream: https://github.com/jdecked/twemoji

Please keep proper Twemoji attribution when redistributing.

## Build from source (maintainers)

Only needed if you want to regenerate fonts locally:

```bash
task init
task install
task
```

Generated files are placed in `fonts/`.
