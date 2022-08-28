from functools import lru_cache
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j):
            if i == m - 1:
                return grid[i][j]
            return grid[i][j] + min(dfs(i+1, k) + moveCost[grid[i][j]][k] for k in range(n))

        return min(dfs(0, j) for j in range(n))


grid = [[5,3],[4,0],[2,1]]
mc = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
print(Solution().minPathCost(grid, mc))