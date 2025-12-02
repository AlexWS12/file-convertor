from pathlib import Path
import xmltodict
import yaml
import json


def xml_to_yaml(src: Path, dst: Path) -> None:
    """XML → YAML (pretty, readable)."""
    text = Path(src).read_text(encoding="utf-8", errors="ignore")
    data = xmltodict.parse(text)
    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)


def yaml_to_xml(src: Path, dst: Path) -> None:
    """YAML → XML.

    Wraps under <root> when needed:
    - dict -> <root>...keys...</root>
    - list -> <root><item>...each...</item></root>
    - scalar -> <root><value>...</value></root>
    """
    with open(src, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if isinstance(data, dict):
        # If there's exactly one top-level key, use it as the root tag
        if len(data) == 1:
            root_name, content = next(iter(data.items()))
            obj = {root_name: content}
        else:
            obj = {"root": data}
    elif isinstance(data, list):
        obj = {"root": {"item": data}}
    else:
        obj = {"root": {"value": data}}

    xml_str = xmltodict.unparse(obj, pretty=True)
    Path(dst).write_text(xml_str, encoding="utf-8")
