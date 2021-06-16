package leetcode

func change(amount int, coins []int) int {
	// dp[i][j] = dp[i-1][j] + dp[i-1][j-money]
	dp := make([]int, amount+1)
	dp[0] = 1
	for _, coin := range coins {
		for j := coin; j <= amount; j++ {
			// for k := 1; k * coin <= j; k++ {
			//     dp[j] += dp[j-k*coin]
			// }
			dp[j] += dp[j-coin]
		}
	}
	return dp[amount]
}
