from core.voice import listen_for_word
from core.arabic_utils import strip_diacritics, words_match

# Take a real word from An-Naba Ayah 1: عَمَّ
expected = "عَمَّ"

print(f"Expected word: {expected}")
print(f"Expected stripped: {strip_diacritics(expected)}")
print()
print("Now say the word...")

spoken = listen_for_word()
print(f"You said: {spoken}")

if spoken:
    print(f"Spoken stripped: {strip_diacritics(spoken)}")
    print(f"Match: {words_match(spoken, expected)}")