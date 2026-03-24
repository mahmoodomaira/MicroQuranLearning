import tkinter as tk

class SurahSelector:
    def __init__(self, parent, surah_list, on_select):
        self.surah_list = surah_list
        self.on_select = on_select

        frame = tk.Frame(parent, bg="#1a1a2e")
        frame.pack(pady=(10, 0))

        label = tk.Label(frame, text="Surah:", font=("Arial", 11),
                         bg="#1a1a2e", fg="#e0c97f")
        label.pack(side=tk.LEFT, padx=(0, 8))

        # Build display names for the dropdown
        self.options = [f"{num}. {name}" for num, name in surah_list]

        self.selected = tk.StringVar(value=self.options[0])
        self.dropdown = tk.OptionMenu(frame, self.selected, *self.options,
                                      command=self._on_change)
        self.dropdown.config(bg="#e0c97f", fg="#1a1a2e", relief="flat",
                             font=("Arial", 11), highlightthickness=0)
        self.dropdown.pack(side=tk.LEFT)
        
    def _on_change(self, selection):
        # Find the index in surah_list that matches the selection
        index = self.options.index(selection)
        surah_number = self.surah_list[index][0]
        self.on_select(surah_number)
        
    def set_surah(self, surah_number):
        for i, (num, name) in enumerate(self.surah_list):
            if num == surah_number:
                self.selected.set(self.options[i])
                break