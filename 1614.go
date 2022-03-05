package leetcode

func maxDepth(s string) int {
	l := byte('(')
	r := byte(')')
	ans := 0
	cur := 0
	for i := 0; i < len(s); i++ {
		if s[i] == l {
			cur += 1
			if cur > ans {
				ans = cur
			}
		} else if s[i] == r {
			cur -= 1
		}
	}
	return ans
}
