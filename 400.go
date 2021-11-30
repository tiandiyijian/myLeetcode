package leetcode

import "math"

func findNthDigit(n int) int {
	d := 1
	count := 9
	for {
		if tmp := d * count; tmp < n {
			n -= tmp
			d++
			count *= 10
		} else {
			break
		}
	}
	idx := (n - 1) / d
	bit := (n - 1) % d
	num := int(math.Pow10(d-1)) + idx
	return num / int(math.Pow10(d-1-bit)) % 10
}
