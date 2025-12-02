from pathlib import Path
import json
import xmltodict


def xml_to_json(src: Path, dst: Path) -> None:
    """XML → JSON (pretty)."""
    with open(src, "r", encoding="utf-8") as f:
        data = xmltodict.parse(f.read())
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def json_to_xml(src: Path, dst: Path) -> None:
    """JSON → XML.

    Wraps top-level in <root> if needed. If the JSON is a list,
    serializes it as <root><item>...</item>...</root>.
    """
    with open(src, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        obj = {"root": {"item": data}}
    elif isinstance(data, dict):
        # ensure single root element
        obj = {"root": data}
    else:
        obj = {"root": {"value": data}}

    xml_str = xmltodict.unparse(obj, pretty=True)
    Path(dst).write_text(xml_str, encoding="utf-8")
