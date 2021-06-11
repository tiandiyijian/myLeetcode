package leetcode

func numSquares(n int) int {
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = i
	}
	for i := 2; i*i <= n; i++ {
		val := i * i
		for j := val; j <= n; j++ {
			dp[j] = min(dp[j], dp[j-val]+1)
		}
	}
	return dp[n]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
