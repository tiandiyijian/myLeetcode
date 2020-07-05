class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens, lenp = len(s), len(p)
        dp = [[False] * (lenp + 1) for _ in range(lens + 1)]
        dp[0][0] = True
        for i in range(1, lenp + 1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-1]
            else:
                break
        for i in range(1, lens + 1):
            for j in range(1, lenp + 1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('aa', '*'))
