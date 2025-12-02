from pathlib import Path
import json


def json_to_toon(src: Path, dst: Path) -> None:
    """JSON → TOON: minified, single-line JSON to reduce tokens/lines."""
    with open(src, "r", encoding="utf-8") as f:
        data = json.load(f)
    text = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(text)


def toon_to_json(src: Path, dst: Path) -> None:
    """TOON → JSON: pretty-printed JSON for readability."""
    with open(src, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
