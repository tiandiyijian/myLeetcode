package leetcode

import "strings"

func toLowerCase(s string) string {
	sb := new(strings.Builder)
	sb.Grow(len(s))
	for _, c := range s {
		if 65 <= c && c <= 90 {
			sb.WriteRune(c + 32)
		} else {
			sb.WriteRune(c)
		}
	}
	return sb.String()
}
