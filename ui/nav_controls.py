import tkinter as tk

class NavControls:
    def __init__(self, parent, callbacks):
        self.frame = tk.Frame(parent, bg="#1a1a2e")
        self.frame.pack(pady=10)

        self.prev_btn = tk.Button(self.frame, text="Previous", command=callbacks["prev"],
                                  bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
        self.prev_btn.pack(side=tk.LEFT, padx=5)

        self.next_btn = tk.Button(self.frame, text="Next", command=callbacks["next"],
                                  bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
        self.next_btn.pack(side=tk.LEFT, padx=5)

        self.memorize_btn = tk.Button(self.frame, text="Memorize", command=callbacks["memorize"],
                                      bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
        self.memorize_btn.pack(side=tk.LEFT, padx=5)

        self.reveal_btn = tk.Button(self.frame, text="Reveal Word", command=callbacks["reveal"],
                                    bg="#e0c97f", fg="#1a1a2e", relief="flat", padx=16, pady=6)
        self.reveal_btn.pack(side=tk.LEFT, padx=5)

    def set_memorize_active(self, active):
        if active:
            self.memorize_btn.config(bg="#c0392b", fg="#ffffff", text="Exit Memorize")
        else:
            self.memorize_btn.config(bg="#e0c97f", fg="#1a1a2e", text="Memorize")