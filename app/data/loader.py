import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "careers.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    CAREERS = json.load(f)
