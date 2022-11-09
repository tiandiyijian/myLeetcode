from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # 只想到暴力枚举每个点当作中心点
        # 但其实可以用dp计算每个点的上下左右各有多少个1
        g = [[1] * (n + 10) for _ in range(n + 10)]
        for x, y in mines:
            g[x + 1][y + 1] = 0
        a, b, c, d = (
            [[0] * (n + 10) for _ in range(n + 10)],
            [[0] * (n + 10) for _ in range(n + 10)],
            [[0] * (n + 10) for _ in range(n + 10)],
            [[0] * (n + 10) for _ in range(n + 10)],
        )
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if g[i][j] == 1:
                    a[i][j] = a[i - 1][j] + 1
                    b[i][j] = b[i][j - 1] + 1
                if g[n + 1 - i][n + 1 - j] == 1:
                    c[n + 1 - i][n + 1 - j] = c[n + 2 - i][n + 1 - j] + 1
                    d[n + 1 - i][n + 1 - j] = d[n + 1 - i][n + 2 - j] + 1
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                ans = max(ans, min(min(a[i][j], b[i][j]), min(c[i][j], d[i][j])))
        return ans
