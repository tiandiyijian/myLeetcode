from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stk = [0]
        for i in range(n - 1, -1, -1):
            while stk[-1] > prices[i]:
                stk.pop()
            ans[i] = prices[i] - stk[-1]
            stk.append(prices[i])
        return ans
