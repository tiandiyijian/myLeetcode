package leetcode

func maximumDifference(nums []int) int {
	ans := -1
	min := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i] <= min {
			min = nums[i]
		} else {
			if tmp := nums[i] - min; tmp > ans {
				ans = tmp
			}
		}
	}
	return ans
}
