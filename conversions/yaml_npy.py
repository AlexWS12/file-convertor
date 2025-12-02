from pathlib import Path
import numpy as np
import yaml


def yaml_to_npy(src: Path, dst: Path) -> None:
    """YAML (list or list-of-lists of numbers) → .npy.

    Simple rules:
    - 1D list becomes one row
    - 2D list stays 2D
    - Values must be numeric (coerced to float)
    """
    with open(src, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    arr = np.asarray(data, dtype=float)
    if arr.ndim == 0:  # scalar → 1x1
        arr = arr.reshape(1, 1)
    elif arr.ndim == 1:  # 1D → 1xN
        arr = arr.reshape(1, -1)

    np.save(dst, arr, allow_pickle=False)


def npy_to_yaml(src: Path, dst: Path) -> None:
    """.npy → YAML (list or list-of-lists)."""
    arr = np.load(src, allow_pickle=False)
    with open(dst, "w", encoding="utf-8") as f:
        yaml.safe_dump(arr.tolist(), f, sort_keys=False, allow_unicode=True)
