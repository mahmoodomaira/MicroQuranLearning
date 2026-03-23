import json
import requests

ARABIC_URL = "https://api.alquran.cloud/v1/juz/30/quran-uthmani"
ENGLISH_URL = "https://api.alquran.cloud/v1/juz/30/en.sahih"
OUTPUT_FILE = "verses.json"


def fetch_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def extract_ayahs(payload):
    """Extract the list of ayahs from the API response."""
    return payload["data"]["ayahs"]


def main():
    print("Fetching Arabic ayahs from:", ARABIC_URL)
    arabic_data = fetch_json(ARABIC_URL)

    print("Fetching English ayahs from:", ENGLISH_URL)
    english_data = fetch_json(ENGLISH_URL)

    arabic_items = extract_ayahs(arabic_data)
    english_items = extract_ayahs(english_data)

    if len(arabic_items) != len(english_items):
        raise ValueError(
            f"Mismatched number of ayahs: arabic={len(arabic_items)}, english={len(english_items)}."
        )

    verses = []

    for arabic_item, english_item in zip(arabic_items, english_items):
        surah = arabic_item["surah"]  # this is a dict like {"number": 78, "englishName": "An-Naba", ...}

        verses.append({
            "surah": surah["number"],
            "surah_name": surah["englishName"],
            "ayah": arabic_item["numberInSurah"],
            "arabic": arabic_item["text"],
            "english": english_item["text"],
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(verses)} verses to {OUTPUT_FILE}")
    print("Sample entry:")
    print(json.dumps(verses[0], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()