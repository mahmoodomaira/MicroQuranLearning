import json
import tkinter as tk

# 1. Load the data
with open("verses.json", encoding="utf-8") as f:
    verses = json.load(f)

# 2. Track the current index
current = 0

def show_verse(index):
    verse = verses[index]
    header_label.config(text=f"{verse['surah_name']} — Ayah {verse['ayah']}")
    arabic_label.config(text=verse['arabic'])
    english_label.config(text=verse['english'])

# 3. Create the main window
root = tk.Tk()
root.title("Quran Reader")
root.geometry("700x400")
root.configure(bg="#1a1a2e")

# 4. Display three labels
header_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#1a1a2e", fg="#e0c97f")
header_label.pack(pady=10)

arabic_label = tk.Label(root, text="", font=("Traditional Arabic", 36), justify="right", anchor="e", bg="#1a1a2e", fg="#e0c97f")
arabic_label.pack(pady=10, fill="x", padx=20)

separator = tk.Frame(root, bg="#e0c97f", height=1)
separator.pack(fill="x", padx=60, pady=8)

english_label = tk.Label(root, text="", font=("Arial", 12), wraplength=600, justify="left", bg="#1a1a2e", fg="#e0c97f")
english_label.pack(pady=10)

# 5. Add two buttons inside a frame
def prev_verse():
    global current
    if current > 0:
        current -= 1
        show_verse(current)

def next_verse():
    global current
    if current < len(verses) - 1:
        current += 1
        show_verse(current)

nav_frame = tk.Frame(root, bg="#1a1a2e")
nav_frame.pack(pady=20)

prev_button = tk.Button(nav_frame, text="Previous", command=prev_verse, bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
prev_button.pack(side=tk.LEFT, padx=20)

next_button = tk.Button(nav_frame, text="Next", command=next_verse, bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
next_button.pack(side=tk.LEFT, padx=20)

# Show the first verse initially
show_verse(current)

# Start the main loop
root.mainloop()

