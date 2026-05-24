#!/usr/bin/env python3
import argparse
import os
import tarfile
import zipfile
from pathlib import Path


def collect_files(src_dir: Path):
    return sorted([p for p in src_dir.rglob("*") if p.is_file()])


def main():
    parser = argparse.ArgumentParser(description="Package font artifacts into tar.gz and zip")
    parser.add_argument("src_dir", help="Source directory to package (e.g. fonts)")
    parser.add_argument("release_dir", help="Output directory for archives (e.g. release)")
    parser.add_argument("basename", help="Archive basename (without extension)")
    args = parser.parse_args()

    src_dir = Path(args.src_dir)
    release_dir = Path(args.release_dir)

    if not src_dir.is_dir():
      raise SystemExit(f"Error: source directory not found: {src_dir}")

    files = collect_files(src_dir)
    if not files:
      raise SystemExit(f"Error: no files found in {src_dir}")

    release_dir.mkdir(parents=True, exist_ok=True)
    tar_path = release_dir / f"{args.basename}.tar.gz"
    zip_path = release_dir / f"{args.basename}.zip"

    with tarfile.open(tar_path, "w:gz") as tf:
        for f in files:
            tf.add(f, arcname=f.relative_to(src_dir))

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=f.relative_to(src_dir))

    print(f"Wrote {tar_path}")
    print(f"Wrote {zip_path}")


if __name__ == "__main__":
    main()
