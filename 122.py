from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i]-prices[i-1])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3]))
