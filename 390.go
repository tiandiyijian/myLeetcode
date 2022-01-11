package leetcode

func lastRemaining(n int) int {
	a1, an := 1, n
	k := 0
	step := 1
	cnt := n
	for cnt > 1 {
		if k&1 == 0 { // 从左向右
			a1 += step
			if cnt&1 == 1 {
				an -= step
			}
		} else { // 从右向左
			an -= step
			if cnt&1 == 1 {
				a1 += step
			}
		}
		cnt /= 2
		k += 1
		step <<= 1
	}
	return a1
}
