package leetcode

func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
	const mod = 1000000007
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, minProfit+1)
		dp[i][0] = 1
	}
	// dp[0][0] = 1
	for i, members := range group {
		earn := profit[i]
		for j := n; j >= members; j-- {
			for k := minProfit; k >= 0; k-- {
				if k < earn {
					dp[j][k] += dp[j-members][0]
				} else {
					dp[j][k] += dp[j-members][k-earn]
				}
				dp[j][k] %= mod
			}
		}
	}
	return dp[n][minProfit]
}
