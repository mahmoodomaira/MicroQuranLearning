class MemorizeController:
    def __init__(self):
        self.active = False
        self.revealed_count = 0

    def toggle(self):
        self.active = not self.active
        self.revealed_count = 0

    def reset(self):
        self.revealed_count = 0

    def reveal_next(self, word_count):
        if self.revealed_count < word_count:
            self.revealed_count += 1

    def get_masked_text(self, arabic_text):
        words = arabic_text.split(" ")
        masked = []
        for i, word in enumerate(words):
            if i < self.revealed_count:
                masked.append(word)
            else:
                masked.append("___")
        return " ".join(masked)
