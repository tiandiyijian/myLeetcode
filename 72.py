class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [[0] * (n+1) for _ in range(m+1)]
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m):
            dp[i+1][0] = i+1
            for j in range(n):
                insert = dp[i+1][j] + 1
                delete = dp[i][j+1] + 1
                if word1[i] == word2[j]:
                    replace = dp[i][j]
                else:
                    replace = dp[i][j] + 1
                dp[i+1][j+1] = min(insert, delete, replace)
        return dp[m][n]