from pathlib import Path
import json
import yaml


def json_to_yaml(src: Path, dst: Path) -> None:
    """Convert a JSON file to YAML (.yaml/.yml)."""
    with open(src, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Writes YAML with readable formatting and preserved key order
    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def yaml_to_json(src: Path, dst: Path) -> None:
    """Convert a YAML/YML file to JSON (.json)."""
    with open(src, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
