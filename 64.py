from typing import List


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for j in range(1, col):
            grid[0][j] += grid[0][j-1]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[row-1][col-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0][:]
        for i in range(1, n):
            dp[i] += dp[i-1]
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
                else:
                    dp[j] += grid[i][j]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(s.minPathSum2(grid))
