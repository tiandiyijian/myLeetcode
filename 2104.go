package leetcode

import "math"

func subArrayRanges(nums []int) int64 {
	// 没想到之前写过，这次刚开始也没想到
	// 但是看题解思路之后自己琢磨出来了
	// 然后看提交记录才想起来自己之前被这道题折磨的不轻
	// 不过这次比上次要好，自己想通了
	// 希望下次碰到单调栈思路更清晰一点
	// 从第一次碰到单调栈这个东西我就感觉它很别扭

	max_sum := int64(0)
	s := []int{-1}
	nums = append(nums, math.MaxInt)
	for i, v := range nums {
		for len(s) > 1 && v >= nums[s[len(s)-1]] {
			j := s[len(s)-1]
			s = s[:len(s)-1]
			right := i - j
			left := j - s[len(s)-1]
			max_sum += int64(left*right) * int64(nums[j])
		}
		s = append(s, i)
	}
	// r := len(nums)
	// for len(s) > 1 {
	//     j := s[len(s)-1]
	//     s = s[:len(s)-1]
	//     right := r - j
	//     left := j - s[len(s)-1]
	//     max_sum += int64(left * right) * int64(nums[j])
	// }

	min_sum := int64(0)
	s = []int{-1}
	nums[len(nums)-1] = math.MinInt
	for i, v := range nums {
		for len(s) > 1 && v <= nums[s[len(s)-1]] {
			j := s[len(s)-1]
			s = s[:len(s)-1]
			right := i - j
			left := j - s[len(s)-1]
			min_sum += int64(left*right) * int64(nums[j])
		}
		s = append(s, i)
	}
	// for len(s) > 1 {
	//     j := s[len(s)-1]
	//     s = s[:len(s)-1]
	//     right := r - j
	//     left := j - s[len(s)-1]
	//     min_sum += int64(left * right) * int64(nums[j])
	// }

	return max_sum - min_sum
}
