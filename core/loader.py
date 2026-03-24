
import json

def load_verses(filepath):
    """Load the verses from the JSON file."""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)