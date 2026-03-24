from email.mime import message
import tkinter as tk

class VerseDisplay:
    def __init__(self, parent):
        self.header_label = tk.Label(parent, text="", font=("Arial", 16, "bold"), fg="#e0c97f", bg="#1a1a2e")
        self.header_label.pack(pady=(10, 5))

        self.arabic_label = tk.Label(parent, text="", font=("Traditional Arabic", 36), fg="#e0c97f", bg="#1a1a2e", anchor="e")
        self.arabic_label.pack(pady=(5, 10))

        separator = tk.Frame(parent, height=1, bg="#e0c97f")
        separator.pack(fill="x", padx=20)

        self.english_label = tk.Label(parent, text="", font=("Arial", 12), fg="#b0b8c1", bg="#1a1a2e", wraplength=600, justify="left")
        self.english_label.pack(pady=(10, 10))
        
        self.status_label = tk.Label(parent, text="", font=("Arial", 11),
                              bg="#1a1a2e", fg="#4a90a4")
        self.status_label.pack(pady=(4, 0))

    def update(self, verse, arabic_text):
        self.header_label.config(text=f"{verse['surah_name']} — Ayah {verse['ayah']}")
        self.arabic_label.config(text=arabic_text)
        self.english_label.config(text=verse['english'])
        
    def set_prayer_mode(self, active):
        if active:
            self.arabic_label.config(font=("Traditional Arabic", 52))
            self.english_label.config(font=("Arial", 14))
        else:
            self.arabic_label.config(font=("Traditional Arabic", 36))
            self.english_label.config(font=("Arial", 12))
            
    def set_status(self, message):
        self.status_label.config(text=message)
