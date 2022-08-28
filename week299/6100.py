class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [1, 1]
        mod = 10**9 + 7
        for i in range(1, n):
            dp[0], dp[1] = (dp[0] + dp[1]) % mod, dp[0] % mod
        
        return (((dp[0] + dp[1]) % mod) ** 2) % mod
        