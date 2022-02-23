package leetcode

import "unicode"

func reverseOnlyLetters(s string) string {
	s1 := []byte(s)
	l, r := 0, len(s)-1
	for l < r {
		b1 := unicode.IsLetter(rune(s1[l]))
		b2 := unicode.IsLetter(rune(s1[r]))
		if b1 && b2 {
			s1[l], s1[r] = s1[r], s1[l]
			l++
			r--
		} else if b1 {
			r--
		} else if b2 {
			l++
		} else {
			l++
			r--
		}
	}
	return string(s1)
}
