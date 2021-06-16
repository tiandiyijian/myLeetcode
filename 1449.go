package leetcode

import "math"

func largestNumber(cost []int, target int) string {
	dp := make([]int, target+1)
	for i := range dp {
		dp[i] = math.MinInt32
	}
	dp[0] = 0
	for _, c := range cost {
		for j := c; j <= target; j++ {
			if tmp := dp[j-c] + 1; tmp > dp[j] {
				dp[j] = tmp
			}
		}
	}
	if dp[target] <= 0 {
		return "0"
	}
	// fmt.Println(dp)
	ans := make([]byte, 0, dp[target])
	for i := 8; i >= 0; i-- {
		for c := cost[i]; target >= c && dp[target-c]+1 == dp[target]; target -= c {
			ans = append(ans, byte('1'+i))
		}
	}
	return string(ans)
}
