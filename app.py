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

# 4. Display three labels
header_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

arabic_label = tk.Label(root, text="", font=("Traditional Arabic", 28), justify="right", anchor="e")
arabic_label.pack(pady=10, fill="x", padx=20)

english_label = tk.Label(root, text="", font=("Arial", 12), wraplength=600, justify="left")
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

nav_frame = tk.Frame(root)
nav_frame.pack(pady=20)

prev_button = tk.Button(nav_frame, text="Previous", command=prev_verse)
prev_button.pack(side=tk.LEFT, padx=20)

next_button = tk.Button(nav_frame, text="Next", command=next_verse)
next_button.pack(side=tk.LEFT, padx=20)

# Show the first verse initially
show_verse(current)

# Start the main loop
root.mainloop()