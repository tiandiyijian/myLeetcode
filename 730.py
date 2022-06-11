class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(n)]
        next = [[-1] * 4 for _ in range(n)]
        pre = [[-1] * 4 for _ in range(n)]

        pos = [-1] * 4
        for i in range(n):
            for c in range(4):
                pre[i][c] = pos[c]
            pos[ord(s[i]) - ord('a')] = i

        pos = [n] * 4
        for i in range(n - 1, -1, -1):
            for c in range(4):
                next[i][c] = pos[c]
            pos[ord(s[i]) - ord('a')] = i

        for i in range(n):
            dp[i][i] = 1

        for sz in range(2, n + 1):
            for j in range(sz - 1, n):
                i = j - sz + 1
                if s[i] == s[j]:
                    low = next[i][ord(s[i]) - ord('a')]
                    high = pre[j][ord(s[j]) - ord('a')]
                    if low > high:
                        # 新增加x和xx两个序列以及dp[i + 1][j - 1]里的以及dp[i + 1][j - 1]里的给它们两端各加上一个x
                        dp[i][j] = (2 + dp[i + 1][j - 1] * 2) % MOD
                    elif low == high:
                        # low=high的时候里面有一个x这个序列所以只加1
                        dp[i][j] = (1 + dp[i + 1][j - 1] * 2) % MOD
                    else:
                        # dp[low][high]以及包括x和xx这两个序列了所以不用加2
                        # dp[low + 1][high - 1]是重复的个数
                        dp[i][j] = (dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]) % MOD
                else:
                    # 容斥原理
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD

        return dp[0][-1]
