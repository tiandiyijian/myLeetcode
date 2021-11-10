package leetcode

func singleNumber(nums []int) []int {
	xor_sum := 0
	for _, num := range nums {
		xor_sum ^= num
	}
	low_bit := xor_sum & (-xor_sum)
	xor_sum_0, xor_sum_1 := 0, 0
	for _, num := range nums {
		if low_bit&num == 0 {
			xor_sum_0 ^= num
		} else {
			xor_sum_1 ^= num
		}
	}
	return []int{xor_sum_0, xor_sum_1}
}
