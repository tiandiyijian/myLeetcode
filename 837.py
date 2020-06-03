class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # if K + W - 1 <= N:
        #     return 1.0
        # elif N < K:
        #     return 0.0
        # dp = [0.0] * (K + W)
        # # for i in range(N+1, K+W-1):
        # #     dp[i] = 0.0
        # for i in range(K, N+1):
        #     dp[i] = 1.0

        # dp[K - 1] = float(min(N - K + 1, W)) / W
        # for i in range(K - 2, -1, -1):
        #     dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        # return dp[0]
        dp = [None]*(K+W)
        s = 0
        for i in range(K, K+W):          # 填蓝色的格子
            dp[i] = 1 if i <= N else 0
            s += dp[i]
        for i in range(K-1, -1, -1):      # 填橘黄色格子
            dp[i] = s/W
            s = s-dp[i+W]+dp[i]
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    print(s.new21Game(6, 1, 10))
