from typing import List

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]))
        # 动态规划条件: 问题能从子问题得到答案
        # 里面用max是指最坏条件
        # 外面用min是指最优策略
        dp = [[0] * (n+1) for _ in range(n+1)]
        for size in range(2, n+1):
            for l in range(1, n-size+2):
                r = l + size - 1
                dp[l][r] = min(k + max(dp[l][k-1], dp[k+1][r] if k < n else 0) for k in range(l, r+1))
        return dp[1][n]

