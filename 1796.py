class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for c in s:
            if c.isdigit():
                n = int(c)
                if n > first:
                    first, second = n, first
                elif second < n < first:
                    second = n
        return second
