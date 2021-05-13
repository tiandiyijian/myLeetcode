package leetcode

func numWays(steps int, arrLen int) int {
	const MOD = 1000000007
	col := steps / 2
	if col >= arrLen {
		col = arrLen - 1
	}
	dp := make([][]int, 2)
	for i := range dp {
		dp[i] = make([]int, col+1)
	}
	dp[0][0] = 1
	for i := 1; i <= steps; i++ {
		row := i & 1
		for j := 0; j <= col; j++ {
			if i == j {
				dp[row][j] = 1
				break
			}
			if i < j {
				break
			}
			dp[row][j] = dp[row^1][j]
			if j > 0 {
				dp[row][j] += dp[row^1][j-1]
				dp[row][j] %= MOD
			}
			if j < col {
				dp[row][j] += dp[row^1][j+1]
				dp[row][j] %= MOD
			}
		}
	}
	return dp[steps&1][0]
}
