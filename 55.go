package leetcode

func canJump(nums []int) bool {
	n := len(nums)
	max_idx := 0
	for i, d := range nums {
		if i > max_idx {
			return false
		}
		if i+d > max_idx {
			max_idx = i + d
		}
		if max_idx >= n-1 {
			return true
		}
	}
	return false
}
