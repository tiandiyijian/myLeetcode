package leetcode

import "sort"

func findKthNumber(m int, n int, k int) int {
	// 考虑对一个数x比它小的数有多少个
	return sort.Search(m*n+1, func(i int) bool {
		cnt := 0
		midRow := i / n
		cnt += midRow * n
		// midRow及之前的行每一行的数字全都小于等于i
		// 之后的行只有一部分小于等于i
		for j := midRow + 1; j <= m; j++ {
			cnt += i / j
		}
		return cnt >= k
	})
}
