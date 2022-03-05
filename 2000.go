package leetcode

import "strings"

func reversePrefix(word string, ch byte) string {
	i := strings.IndexByte(word, ch)
	if i < 0 {
		return word
	}
	s := []byte(word)
	for left, right := 0, i; left < right; left++ {
		s[left], s[right] = s[right], s[left]
		right--
	}
	return string(s)
}
