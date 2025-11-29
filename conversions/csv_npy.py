from pathlib import Path
import csv
import numpy as np


def csv_to_npy(src: Path, dst: Path):
    rows = []

    with src.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue

            numeric_values = []
            for x in row:
                try:
                    numeric_values.append(float(x))
                except ValueError:
                    # skip non numeric values (like headers or text columns)
                    continue

            if numeric_values:
                rows.append(numeric_values)

    arr = np.array(rows, dtype=float)
    np.save(dst, arr)
