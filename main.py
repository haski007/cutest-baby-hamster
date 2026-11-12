"""Entry for make.fun bounty cutest-picture-01.

Copies the picture that sits next to this file to <output dir>/entry.png,
byte for byte. Standard library only, no network, deterministic.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: picture not found: {SOURCE}", file=sys.stderr)
        return 1
    data = SOURCE.read_bytes()
    # The gate accepts only a PNG or a JPEG of at most 1 MiB: refuse anything else.
    if not data.startswith((PNG_MAGIC, JPEG_MAGIC)):
        print("error: picture is neither a PNG nor a JPEG", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: picture is {len(data)} bytes, over {MAX_BYTES}", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
