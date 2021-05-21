package main

import (
	"fmt"
)

/*
 * @lc app=leetcode.cn id=1035 lang=golang
 *
 * [1035] 不相交的线
 */

// @lc code=start
func maxUncrossedLines(nums1 []int, nums2 []int) int {
	m, n := len(nums1), len(nums2)
	dp := make([][]int, m+1)
	dp[0] = make([]int, n+1)
	for i := 1; i <= m; i++ {
		dp[i] = make([]int, n+1)
		for j := 1; j <= n; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[m][n]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// @lc code=end
func main() {
	nums1 := []int{1, 4, 2}
	nums2 := []int{1, 2, 4}
	fmt.Println(maxUncrossedLines(nums1, nums2))
}
