# MicroQuranLearning

A small Quran verse fetcher and reader UI using Python, `requests`, and `tkinter`.

## Features

- Fetch Arabic + English ayahs from remote JSON API endpoints (`fetch_verses.py`)
- Merge data into a normalized `verses.json`
- Simple GUI reader (`app.py`) using `tkinter` with Previous/Next navigation

## Files

- `fetch_verses.py` - Fetch data from two URLs, merge by index, write `verses.json`
- `app.py` - Load `verses.json`, display current ayah, navigate between ayahs
- `verses.json` - Generated verse data (not committed unless you choose)
- `README.md` - This documentation

## Setup

1. Ensure Python 3.11+ (or 3.10+) is installed
2. Create virtual environment (recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install requests
```

## Usage

### 1) Fetch verses

Edit `fetch_verses.py` and set:

- `ARABIC_URL` to your Arabic API endpoint
- `ENGLISH_URL` to your English (translation) API endpoint

Then run:

```bash
python fetch_verses.py
```

This outputs `verses.json` with:
- `surah`
- `surah_name`
- `ayah`
- `arabic`
- `english`

### 2) Run GUI

```bash
python app.py
```

Buttons:
- Previous
- Next

## Notes

- `verses.json` can become large if you sync full Quran; add to `.gitignore` if needed.
- Run `git init`, add files, commit, and push to your GitHub remote as described earlier.

## GitHub setup

From repo root:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/MicroQuranLearning.git
git push -u origin main
```

## License

MIT (or choose preferred license)
