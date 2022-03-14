package leetcode

func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])
	if obstacleGrid[m-1][n-1] == 1 {
		return 0
	}

	dp := make([]int, n)
	dp[0] = 1
	for i := 0; i < m; i++ {
		if obstacleGrid[i][0] == 1 {
			dp[0] = 0
		}
		for j := 1; j < n; j++ {
			if obstacleGrid[i][j] == 1 {
				dp[j] = 0
				continue
			} else {
				dp[j] += dp[j-1]
			}
		}
	}

	return dp[n-1]
}
