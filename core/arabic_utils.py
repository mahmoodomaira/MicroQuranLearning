import unicodedata

def strip_diacritics(text):
    """Remove Arabic diacritics (tashkeel) from text."""
    return "".join(
        ch for ch in text
        if unicodedata.category(ch) != 'Mn'
    )

def words_match(spoken, expected):
    """Loose match between two single words."""
    s = strip_diacritics(spoken.strip())
    e = strip_diacritics(expected.strip())
    return s == e or s.startswith(e) or e.startswith(s)

def score_recitation(spoken, expected_arabic):
    """
    Compare a spoken sentence to a full Arabic verse.
    Returns (matched_count, total_count).
    """
    spoken_words = strip_diacritics(spoken).split()
    expected_words = strip_diacritics(expected_arabic).split()
    matched = sum(
        1 for e in expected_words
        if any(words_match(s, e) for s in spoken_words)
    )
    return matched, len(expected_words)