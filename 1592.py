class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        words = text.split()
        l = sum(len(w) for w in words)

        if len(words) == 1:
            return words[0] + ' ' * (n - l)

        cnt, left = divmod(n - l, len(words) - 1)
        # left = (n - l) % (len(words) - 1)
        return (' ' * cnt).join(words) + ' ' * left
