package leetcode

import (
	"math"
)

/*
 * @lc app=leetcode.cn id=664 lang=golang
 *
 * [664] 奇怪的打印机
 */

// @lc code=start
func strangePrinter(s string) int {
	n := len(s)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}
	for size := 2; size <= n; size++ {
		for i := 0; i <= n-size; i++ {
			j := i + size - 1
			if s[i] == s[j] {
				dp[i][j] = dp[i+1][j] // 此时dp[i][j-1] = dp[i+1][j]
			} else {
				dp[i][j] = math.MaxInt64
				for k := i; k < j; k++ {
					dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
				}
			}
		}
	}
	// fmt.Println(dp)
	return dp[0][n-1]
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

// @lc code=end
