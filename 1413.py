from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minS = 1
        s = 0
        for n in nums:
            s += n
            if s < minS:
                minS = s

        return 1 if minS > 0 else -minS + 1
