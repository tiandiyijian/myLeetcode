from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = [c.lower() for c in licensePlate if c.isalpha()]
        C0 = Counter(licensePlate)
        ans = None
        ans_len = float('inf')
        for w in words:
            if len(w) < ans_len:
                if not C0 - Counter(w):
                    ans = w
                    ans_len = len(ans)
        return ans
