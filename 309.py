from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i_0 = 0
        i_1 = -sys.maxsize - 1 #还没开始不能买股票，如果设为0那就相当于一开始白嫖了，因为如果一开始买了股票那么手里的钱肯定是负数啊
        i_0_pre = 0
        for i in range(len(prices)):
            tmp = i_0
            i_0 = max(i_0, i_1 + prices[i])
            i_1 = max(i_1, i_0_pre - prices[i])
            i_0_pre = tmp
        return i_0


if __name__ == "__main__":
    s = Solution()
    l = [1,2,3]
    print(s.maxProfit(l))