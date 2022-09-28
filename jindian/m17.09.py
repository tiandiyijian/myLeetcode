class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [1] * k
        p3 = p5 = p7 = 0

        for i in range(1, k):
            nxt = min(dp[p3] * 3, dp[p5] * 5, dp[p7] * 7)
            dp[i] = nxt
            # 防止重复
            if dp[p3] * 3 == nxt:
                p3 += 1
            if dp[p5] * 5 == nxt:
                p5 += 1
            if dp[p7] * 7 == nxt:
                p7 += 1

        return dp[-1]
