class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set('aeiouAEIOU')
        return sum(c in vowels for c in s[: n // 2]) == sum(
            c in vowels for c in s[n // 2 :]
        )
