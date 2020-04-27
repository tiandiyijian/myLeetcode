class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices: return 0
        ans = 0
        tmp_min = prices[0]
        # for i in range(len(prices)):
        #     tmp_min = min(tmp_min, prices[i])
        #     ans = max(ans, prices[i] - tmp_min)
        # for p in prices:
        #     tmp_min = min(tmp_min, p)
        #     ans = max(ans, p - tmp_min)
        for p in prices:
            if p < tmp_min:
                tmp_min = p
            else:
                ans = max(ans, p - tmp_min)
        return ans
