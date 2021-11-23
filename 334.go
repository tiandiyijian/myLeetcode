package leetcode

import "math"

func increasingTriplet(nums []int) bool {
	n := len(nums)
	if n < 3 {
		return false
	}
	small, mid := math.MaxInt32, math.MaxInt32
	for _, num := range nums {
		if num <= small {
			small = num
		} else if num <= mid {
			mid = num
		} else {
			return true
		}
	}
	return false
}
