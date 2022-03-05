package leetcode

func longestNiceSubstring(s string) string {
	ans := ""
	n := len(s)
	for l := 0; l < n; l++ {
		a, b := 0, 0
		for r := l; r < n; r++ {
			if s[r] >= 'a' && s[r] <= 'z' {
				a |= (1 << (s[r] - 'a'))
			} else {
				b |= (1 << (s[r] - 'A'))
			}
			if a == b && r-l+1 > len(ans) {
				ans = s[l : r+1]
			}
		}
	}
	return ans
}
