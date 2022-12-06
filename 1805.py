class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ints = set()
        cur = None
        for c in word:
            if c.isdigit():
                if cur is None:
                    cur = 0
                cur = cur * 10 + ord(c) - ord('0')
            else:
                if cur is not None:
                    ints.add(cur)
                    cur = None
        if cur is not None:
            ints.add(cur)
        return len(ints)
