package leetcode

func findMin(nums []int) int {
	if nums[0] < nums[len(nums)-1] {
		return nums[0]
	}
	// return nums[sort.Search(len(nums)-1, func(i int) bool {
	// 	return nums[i] < nums[0]
	// })]
	i, j := 0, len(nums)-1
	for i < j {
		mid := int(uint(i+j) >> 1)
		if nums[mid] < nums[0] {
			j = mid
		} else {
			i = mid + 1
		}
	}
	return nums[i]
}
