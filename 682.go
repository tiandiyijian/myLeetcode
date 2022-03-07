package leetcode

import (
	"strconv"
)

func calPoints(ops []string) int {
	ans := 0
	s := []int{}
	for _, str := range ops {
		switch str {
		case "C":
			s = s[:len(s)-1]
		case "D":
			s = append(s, s[len(s)-1]<<1)
		case "+":
			s = append(s, s[len(s)-1]+s[len(s)-2])
		default:
			num, _ := strconv.Atoi(str)
			s = append(s, num)
		}
	}
	for _, v := range s {
		ans += v
	}
	return ans
}
