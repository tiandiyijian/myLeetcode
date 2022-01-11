package leetcode

import "strings"

func modifyString(s string) string {
	var sb strings.Builder
	n := len(s)
	sb.Grow(n)
	pre_rune := '0'
	for i, r := range s {
		if r == '?' {
			for j := 'a'; j <= 'z'; j++ {
				if i > 0 && j == pre_rune {
					continue
				}
				if i < n-1 && j == rune(s[i+1]) {
					continue
				}
				sb.WriteRune(j)
				pre_rune = j
				break
			}
		} else {
			sb.WriteRune(r)
			pre_rune = r
		}
	}
	return sb.String()
}
