from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        # 看见对角线就默认当作是左上到右下的了
        # 结果错了两次, 艹
        # for i in range(n):
        #     if grid[i][i] == 0 or grid[i][n-1-i] == 0:
        #         return False
        # for i in range(1, n-1):
        #     if grid[0][i] != 0 or grid[i][0] != 0 or grid[n-1][i] != 0 or grid[i][n-1] != 0:
        #         return False
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
