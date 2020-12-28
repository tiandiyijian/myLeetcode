from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [float("-inf")] * (k + 1)
        sell = [float("-inf")] * (k + 1)

        buy[0], sell[0] = -prices[0], 0
        # for i in range(1, k + 1):
        #     buy[i] = sell[i] = float("-inf")

        for i in range(1, n):
            buy[0] = max(buy[0], sell[0] - prices[i])
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j] - prices[i])
                sell[j] = max(sell[j], buy[j - 1] + prices[i])
            # print(buy, sell)
        # print(sell)
        return sell[-1]


if __name__ == "__main__":
    s = Solution()
    k = 2
    prices = [1, 2, 4, 7]
    print(s.maxProfit(k, prices))
