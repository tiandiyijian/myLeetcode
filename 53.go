package leetcode

func maxSubArray(nums []int) int {
	max := -10001
	ans := max
	for i := 0; i < len(nums); i++ {
		if tmp := max + nums[i]; tmp > nums[i] {
			max = tmp
		} else {
			max = nums[i]
		}
		// fmt.Println(nums[i], max)
		if max > ans {
			ans = max
		}
	}
	return ans
}
