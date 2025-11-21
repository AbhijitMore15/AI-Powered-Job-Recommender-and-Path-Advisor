import json
import csv
import os
from typing import List, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # app/
DATA_DIR = os.path.join(BASE_DIR, "data")


def _json_path(filename: str) -> str:
    return os.path.join(DATA_DIR, filename)


def load_careers_json(filename: str = "careers.json") -> List[Dict[str, Any]]:
    """
    Load careers from JSON. Returns list of career dicts.
    """
    path = _json_path(filename)
    if not os.path.exists(path):
        # try alternate filename (some users name it career.json or expanded_careers.json)
        alt_files = ["careers.json", "career.json", "expanded_careers.json", "all_careers_dataset.json"]
        for f in alt_files:
            alt = _json_path(f)
            if os.path.exists(alt):
                path = alt
                break

    if not os.path.exists(path):
        # Return empty list and log for safety — don't crash the app on import
        print(f"[data_loader] WARNING: JSON dataset not found at {path}")
        return []

    with open(path, "r", encoding="utf-8") as fh:
        try:
            data = json.load(fh)
            # If stored as { "careers": [...] } handle that too
            if isinstance(data, dict) and "careers" in data:
                return data["careers"]
            return data
        except json.JSONDecodeError as e:
            print(f"[data_loader] ERROR: JSON decode error for {path}: {e}")
            return []


def load_careers_csv(filename: str = "careers.csv") -> List[Dict[str, Any]]:
    """
    Load careers from CSV. Returns list of row dicts.
    """
    path = _json_path(filename)
    if not os.path.exists(path):
        alt_files = ["careers.csv", "career.csv", "expanded_careers.csv", "all_careers_dataset.csv"]
        for f in alt_files:
            alt = _json_path(f)
            if os.path.exists(alt):
                path = alt
                break

    if not os.path.exists(path):
        print(f"[data_loader] WARNING: CSV dataset not found at {path}")
        return []

    rows: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            rows.append(dict(r))
    return rows
def get_all_careers():
    return CAREERS
