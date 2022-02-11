package leetcode

import "sort"

func minimumDifference(nums []int, k int) int {
	sort.Ints(nums)
	ans := 100000
	for i := 0; i+k <= len(nums); i++ {
		if tmp := nums[i+k-1] - nums[i]; tmp < ans {
			ans = tmp
		}
	}
	return ans
}
