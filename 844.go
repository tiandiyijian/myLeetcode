package leetcode

func backspaceCompare(s string, t string) bool {
	i, j := len(s)-1, len(t)-1
	for i >= 0 || j >= 0 {
		if i >= 0 && s[i] == '#' {
			cnt := 0
			for i >= 0 && (s[i] == '#' || cnt > 0) {
				if s[i] == '#' {
					cnt++
				} else {
					cnt--
				}
				i--
			}
		}
		if j >= 0 && t[j] == '#' {
			cnt := 0
			for j >= 0 && (t[j] == '#' || cnt > 0) {
				if t[j] == '#' {
					cnt++
				} else {
					cnt--
				}
				j--
			}
		}
		// fmt.Println(i, j)
		if i < 0 && j < 0 {
			return true
		} else if i >= 0 && j >= 0 {
			if s[i] != t[j] {
				return false
			}
			i--
			j--
		} else {
			return false
		}
	}
	return true
}
