class Solution:
    def numTilings(self, n: int) -> int:
        mod = 1000000007
        dp = [[0] * 4 for _ in range(n + 1)]  # 4个state分别是上下都没有、只有上面有、只有下面有、上下都有
        dp[0][3] = 1

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][3]
            dp[i][1] = (dp[i - 1][2] + dp[i - 1][0]) % mod
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][0]) % mod
            dp[i][3] = (dp[i - 1][3] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][0]) % mod

        return dp[-1][-1]
