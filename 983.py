from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        for i in range(1, days[-1]+1):
            if i in days:
                dp[i] = min(dp[i-1] + costs[0], dp[i-7] +
                            costs[1], dp[i-30] + costs[2])
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[days[-1]]


if __name__ == "__main__":
    s = Solution()
    d = [1, 4, 6, 7, 8, 20]
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    c = [2, 7, 15]
    print(s.mincostTickets(d, c))
