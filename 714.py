class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        own, not_own = -prices[0], 0
        for i in range(1, len(prices)):
            own, not_own = max(
                own, not_own - prices[i]), max(not_own, own + prices[i] - fee)
        return not_own


if __name__ == "__main__":
    s = Solution()
    print()
