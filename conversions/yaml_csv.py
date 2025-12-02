from pathlib import Path
import csv
import yaml


def yaml_to_csv(src: Path, dst: Path) -> None:
    """YAML → CSV (simple rules).

    - list of dicts  -> header from first dict's keys
    - list of scalars -> one column named "value"
    - list of lists  -> rows as-is
    """
    with open(src, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, list):
        raise ValueError("YAML must be a list to convert to CSV")

    # list of dicts
    if data and isinstance(data[0], dict):
        headers = list(data[0].keys())
        with open(dst, "w", newline="", encoding="utf-8") as out:
            w = csv.DictWriter(out, fieldnames=headers)
            w.writeheader()
            for row in data:
                w.writerow({k: row.get(k, "") for k in headers})
        return

    # list of scalars
    if data and not isinstance(data[0], (list, dict)):
        with open(dst, "w", newline="", encoding="utf-8") as out:
            w = csv.writer(out)
            w.writerow(["value"])  # header
            for item in data:
                w.writerow([item])
        return

    # list of lists (or empty)
    with open(dst, "w", newline="", encoding="utf-8") as out:
        w = csv.writer(out)
        for row in data:
            w.writerow(row if isinstance(row, list) else [row])


def csv_to_yaml(src: Path, dst: Path) -> None:
    """CSV → YAML (list of lists, keep strings)."""
    rows = []
    with open(src, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            rows.append(list(row))
    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(rows, f, sort_keys=False, allow_unicode=True)
