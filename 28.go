package leetcode

func strStr(haystack string, needle string) int {
	m, n := len(haystack), len(needle)
	next := make([]int, n)
	i := 1
	now := 0
	for i < n {
		if needle[i] == needle[now] {
			now++
			next[i] = now
			i++
		} else if now > 0 {
			now = next[now-1]
		} else {
			i++
		}
	}
	// fmt.Println(next)
	p := 0
	for q := 0; q < m; {
		if haystack[q] == needle[p] {
			p++
			q++
		} else if p > 0 {
			p = next[p-1]
		} else {
			q++
		}
		// fmt.Println(p, q)
		if p == n {
			return q - n
		}
	}
	return -1
}
