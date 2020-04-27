class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        if obstacleGrid == [[1]] :
            return 0
        row = len(obstacleGrid)
        if row == 0:
            return 0
        col = len(obstacleGrid[0])
        self.sum = 0
        self.walk(0, 0, row - 1, col - 1, obstacleGrid)
        return self.sum

    def walk(self, i, j, ti, tj, grid):
        if i == ti and j == tj:
            self.sum += 1
        if i < ti and grid[i+1][j] == 0:
            self.walk(i+1, j, ti, tj, grid)
        if j < tj and grid[i][j+1] == 0:
            self.walk(i, j+1, ti, tj, grid)
        """
        row = len(obstacleGrid)
        if row == 0 or obstacleGrid[0][0] == 1:
            return 0
        col = len(obstacleGrid[0])
        res = [[0 for i in range(col) for j in range(row)]]
        res[1][1] = 1
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if obstacleGrid[i-1][j-1] == 0:
                    res[i][j] += res[i-1][j]
                    res[i][j] += res[i][j-1]
        return res[row][col]