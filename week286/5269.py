from functools import lru_cache
from typing import List


class Solution:

    def maxValueOfCoins1(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # indices = [0] * n
        ans = 0

        @lru_cache(None)
        def dfs(op, cur, indices):
            if op == k:
                nonlocal ans
                ans = max(ans, cur)
                return
            # print(op, cur)
            for i in range(n):
                if indices[i] < len(piles[i]):
                    # indices[i] += 1

                    dfs(
                        op + 1, cur + piles[i][indices[i]],
                        tuple(indices[j] + (0 if j != i else 1)
                              for j in range(n)))
                    # indices[i] -= 1

        dfs(0, 0, (0, ) * n)
        return ans

    def maxValueOfCoins2(self, piles: List[List[int]], k: int) -> int:
        # 完全想错方向了
        n = len(piles)
        dp = [[[0, [0] * n] for _ in range(n)] for i in range(k)]
        for i in range(k):

            for j in range(n):
                if i == 0:
                    dp[i][j][0] = piles[j][0]
                    dp[i][j][1][j] += 1
                    continue
                for p in range(n):
                    if dp[i - 1][p][1][j] < len(piles[j]):
                        if (tmp := dp[i - 1][p][0] +
                                piles[j][dp[i - 1][p][1][j]]) > dp[i][j][0]:
                            dp[i][j][0] = tmp
                            dp[i][j][1] = dp[i - 1][p][1][:]
                            dp[i][j][1][j] += 1
        return max(dp[k - 1][j][0] for j in range(n))

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # 当作背包问题
        # dp[i][j]是从第1到i个背包中取j个硬币的价值
        # dp[i][j] = max(dp[i-1][j-w] + piles[i][w])
        n = len(piles)
        f = [0] * (k + 1)
        sum_n = 0
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i - 1]
            sum_n = min(sum_n + len(pile), k)
            for i in range(sum_n, 0, -1):
                f[i] = max(
                    f[i],
                    max(f[i - w - 1] + pile[w]  ## 因为w是从0开始的，所以要再减一
                        for w in range(min(len(pile), i))))
        return f[k]


piles = [[80, 62, 78, 78, 40, 59, 98, 35], [79, 19, 100, 15],
         [
             79, 2, 27, 73, 12, 13, 11, 37, 27, 55, 54, 55, 87, 10, 97, 26, 78,
             20, 75, 23, 46, 94, 56, 32, 14, 70, 70, 37, 60, 46, 1, 53
         ]]
k = 25
print(Solution().maxValueOfCoins(piles, k))