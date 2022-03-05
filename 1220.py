class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [1] * 5
        for i in range(1, n):
            tmp = [0] * 5
            tmp[0] = (dp[1] + dp[2] + dp[4]) % mod
            tmp[1] = (dp[0] + dp[2]) % mod
            tmp[2] = (dp[1] + dp[3]) % mod
            tmp[3] = dp[2] % mod
            tmp[4] = (dp[2] + dp[3]) % mod
            dp = tmp
        return sum(dp) % mod