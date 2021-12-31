package leetcode

import "math"

func checkPerfectNumber(num int) bool {
	if num == 1 {
		return false
	}
	sum := 1
	for i := 2; i < int(math.Sqrt(float64(num)))+1; i++ {
		if num%i == 0 {
			sum += i
			if tmp := num / i; tmp != i {
				sum += tmp
			}
		}
	}
	return sum == num
}
