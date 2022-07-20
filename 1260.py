from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        size = m * n

        for i in range(m):
            for j in range(n):
                pos = (i * n + j + k) % size
                ans[pos // n][pos % n] = grid[i][j]

        return ans
