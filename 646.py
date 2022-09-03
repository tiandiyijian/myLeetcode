from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[1], x[0]))
        ans = 0
        cur = float('-inf')

        for start, end in pairs:
            if start > cur:
                cur = end
                ans += 1

        return ans
