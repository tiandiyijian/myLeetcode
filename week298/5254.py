from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # 参考https://leetcode.cn/problems/selling-pieces-of-wood/solution/by-tsreaper-m7i7/
        # 记录直接卖的收益
        A = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            A[h][w] = p

        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 直接卖
                f[i][j] = A[i][j]
                # 沿水平方向分割
                for k in range(1, i):
                    f[i][j] = max(f[i][j], f[k][j] + f[i - k][j])
                # 沿垂直方向分割
                for k in range(1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[i][j - k])

        return f[m][n]
