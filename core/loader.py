
import json

def load_verses(filepath):
    """Load the verses from the JSON file."""
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)
    
    
def get_surah_list(verses):
    """Return a list of unique surahs in order: [(number, name), ...]"""
    seen = []
    result = []
    for verse in verses:
        if verse["surah"] not in seen:
            seen.append(verse["surah"])
            result.append((verse["surah"], verse["surah_name"]))
    return result