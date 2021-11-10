package leetcode

func missingNumber(nums []int) int {
	n := len(nums) + 1
	sum := n * (n - 1) / 2
	for _, num := range nums {
		sum -= num
	}
	return sum
}
