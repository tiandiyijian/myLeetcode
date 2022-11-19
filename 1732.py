from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        start = 0
        for g in gain:
            start += g
            ans = max(ans, start)

        return ans
