class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for i in range(1, m+1):
            print(dp[i][1:n+1])
        return m + n - 2 * dp[m][n]

    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [0] * (n+1)
        for i in range(m):
            tem = dp.copy()
            for j in range(1, n + 1):
                if word2[j-1] == word1[i]:
                    dp[j] = tem[j-1] + 1
                else:
                    dp[j] = max(dp[j-1], dp[j])
            print(dp[1:])
        return m + n - 2 * dp[n]

    def lcs(self, word1, word2, m, n):
        if m == 0 or n == 0:
            return 0
        if word1[m-1] == word2[n-1]:
            return 1 + self.lcs(word1, word2, m-1, n-1)
        else:
            return max(self.lcs(word1, word2, m-1, n), self.lcs(word1, word2, m, n-1))

def fib(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def fib1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    fib1 = fib2 = 1
    for i in range(n-2):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2

if __name__ == '__main__':
    s = Solution()
    w1 = 'intention'
    w2 = 'execution'
    print(s.minDistance2(w1, w2))
    # for i in range(1, 10):
    #     print(fib(i), fib1(i))
    print(s.lcs(w1, w2, len(w1), len(w2)))