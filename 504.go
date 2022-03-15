package leetcode

import "strings"

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	if num < 0 {
		return "-" + convertToBase7(-num)
	}

	chars := []byte{}
	for num > 0 {
		chars = append(chars, byte(num%7)+'0')
		num /= 7
	}

	var sb strings.Builder
	for i := len(chars) - 1; i >= 0; i-- {
		sb.WriteByte(chars[i])
	}
	return sb.String()
}
