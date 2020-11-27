from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = Counter(a + b for a in A for b in B)
        ans = 0
        for c in C:
            for d in D:
                ans += counter.get(-c - d, 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()