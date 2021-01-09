from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if not prices:
        #     return 0
        # profits = []
        # tmpMin = prices[0]
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] >= prices[i-1]:
        #         profit += prices[i] - prices[i-1]
        #     else:
        #         profits.append(profit)
        #         profit = 0
        # profits.append(profit)
        # print(profits)
        # profits.sort()
        # return sum(profits[-2:])
        if not prices:
            return 0
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0

        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2


if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 3, 4, 5]
    l = [3, 3, 5, 0, 0, 3, 1, 4]
    l = [7, 6, 4, 3, 1]
    l = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    print(s.maxProfit(l))
