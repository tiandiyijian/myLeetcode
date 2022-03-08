package leetcode

func findKthLargest(nums []int, k int) int {
	n := len(nums)
	lo, hi := 0, n
	target := n - k
	for {
		p := paration(nums, lo, hi)
		if p == target {
			return nums[p]
		} else if p < target {
			lo = p + 1
		} else {
			hi = p - 1
		}
	}
}

func paration(nums []int, lo, hi int) int {
	pivot := nums[lo]
	i := 0
	for j := lo; j < hi; j++ {
		if nums[j] <= pivot {
			nums[j], nums[i] = nums[i], nums[j]
			i++
		}
	}
	i--
	nums[lo], nums[i] = nums[i], nums[lo]
	return i
}
