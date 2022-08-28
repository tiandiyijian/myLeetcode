from typing import List


class Solution:

    def projectionArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xy = 0
        xz = sum(max(row) for row in grid)
        yz = 0
        for i in range(n):
            curMax = 0
            for j in range(m):
                if grid[j][i] > 0:
                    curMax = max(grid[j][i], curMax)
                    xy += 1
            yz += curMax
        return xy + yz + xz