package leetcode

func lastStoneWeightII(stones []int) int {
	sum := 0
	for _, val := range stones {
		sum += val
	}
	max_neg := sum / 2
	dp := make([]bool, max_neg+1)
	dp[0] = true
	for _, weight := range stones {
		for j := max_neg; j >= weight; j-- {
			dp[j] = dp[j] || dp[j-weight]
		}
	}
	for i := max_neg; i >= 0; i-- {
		if dp[i] {
			return sum - 2*i
		}
	}
	return sum
}
