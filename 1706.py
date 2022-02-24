from typing import List


class Solution:

    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            # if i == m:
            #     return 1
            while i < m:
                if (j == 0 and grid[i][j] == -1) or\
                    (j == n-1 and grid[i][j] == 1) or\
                    (grid[i][j] == 1 and j < n-1 and grid[i][j+1] == -1) or\
                    (grid[i][j] == -1 and j > 0 and grid[i][j-1] == 1):
                    return -1
                if i == m - 1:
                    return j + 1 if grid[i][j] == 1 else j - 1
                if grid[i][j] == 1:
                    j += 1
                else:
                    j -= 1
                i += 1

        return [dfs(0, j) for j in range(n)]
