package leetcode

func checkSubarraySum(nums []int, k int) bool {
	pre := map[int]int{0: -1}
	sum := 0
	for i, val := range nums {
		if nums[i] == 0 && i > 0 && nums[i-1] == 0 {
			return true
		}
		sum = (sum + val) % k
		if ix, ok := pre[sum]; ok {
			if i-ix > 1 {
				return true
			}
		} else {
			pre[sum] = i
		}
	}
	return false
}
