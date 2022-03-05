package leetcode

func dominantIndex(nums []int) int {
	a, b := -1, -2
	ia := -1
	for i, num := range nums {
		if num > a {
			a, b = num, a
			ia = i
		} else if num > b {
			b = num
		}
	}
	if a >= b<<1 {
		return ia
	}
	return -1
}
