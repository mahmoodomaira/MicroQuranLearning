import tkinter as tk
from core.memorize import MemorizeController
from ui.verse_display import VerseDisplay
from ui.nav_controls import NavControls

class AppWindow:
    def __init__(self, verses):
        self.verses = verses
        self.current = 0
        self.memorize = MemorizeController()

        root = tk.Tk()
        root.title("Micro Quran Learning")
        root.geometry("800x600")
        root.configure(bg="#1a1a2e")

        self.display = VerseDisplay(root)
        callbacks = {
            "prev": self.prev_verse,
            "next": self.next_verse,
            "memorize": self.toggle_memorize,
            "reveal": self.reveal_next
        }
        self.nav = NavControls(root, callbacks)

        self.show_verse(0)
        root.mainloop()

    def show_verse(self, index):
        verse = self.verses[index]
        if self.memorize.active:
            arabic = self.memorize.get_masked_text(verse['arabic'])
        else:
            arabic = verse['arabic']
        self.display.update(verse, arabic)

    def prev_verse(self):
        if self.current > 0:
            self.current -= 1
            self.memorize.reset()
            self.show_verse(self.current)

    def next_verse(self):
        if self.current < len(self.verses) - 1:
            self.current += 1
            self.memorize.reset()
            self.show_verse(self.current)

    def toggle_memorize(self):
        self.memorize.toggle()
        self.nav.set_memorize_active(self.memorize.active)
        self.show_verse(self.current)

    def reveal_next(self):
        word_count = len(self.verses[self.current]['arabic'].split(" "))
        self.memorize.reveal_next(word_count)
        self.show_verse(self.current)