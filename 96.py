class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            tmp = 0
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                tmp += dp[left] * dp[right]
            dp[i] = tmp
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(4))
