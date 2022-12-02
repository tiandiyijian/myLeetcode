class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        # dp[i][j][len]表示从s1下标i开始长度为len的字符串是否能变换为从s2下标j开始长度为len的字符串
        # 本来应该用dp[i][j][p][q]表示从s1[i:j]能否变为s2[p:q]
        # 但是j-i肯定等于q-p，所以可以用dp[i][p][len]三个状态来表示
        # 感觉跟之前做过的dp不一样的地方在于i和p可以是不相等的
        # 因为存在交换前后位置的情况

        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for size in range(2, n + 1):
            for i in range(n - size + 1):
                for j in range(n - size + 1):
                    for k in range(1, size):
                        a = dp[i][j][k] and dp[i + k][j + k][size - k]  # 不交换
                        b = dp[i][j + size - k][k] and dp[i + k][j][size - k]  # 交换
                        dp[i][j][size] = a or b
                        if dp[i][j][size]:
                            break

        # print(dp)
        return dp[0][0][n]


s1 = "abcde"
s2 = "caebd"
print(Solution().isScramble(s1, s2))
