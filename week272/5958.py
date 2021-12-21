from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        def helper(n: int) -> int:
            return (n * (n+1)) >> 1
        ans = 0
        n = len(prices)
        l = 0
        while l < n:
            r = l + 1
            while r < n and prices[r] == prices[r-1] - 1:
                r += 1
            ans += helper(r-l)
            l = r
        return ans


prices = [8]
print(Solution().getDescentPeriods(prices))
