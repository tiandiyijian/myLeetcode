package leetcode

import "sort"

func singleNonDuplicate(nums []int) int {
	n := len(nums)
	return nums[sort.Search(n>>1, func(i int) bool {
		return nums[2*i] != nums[2*i+1]
	})*2]
}
