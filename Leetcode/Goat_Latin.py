class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        for i, word in enumerate(words):
            if word[0].lower() in {"a", "e", "i", "o", "u"}:
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            words[i] = word + "a" * (i + 1)
        return " ".join(words)
