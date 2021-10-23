package leetcode

func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] != 9 {
			digits[i] += 1
			return digits
		} else {
			digits[i] = 0
		}
	}
	if digits[0] == 0 {
		digits[0] = 1
		return append(digits, 0)
	}
	return digits
}
