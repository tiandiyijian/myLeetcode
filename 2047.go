package leetcode

import (
	"strings"
	"unicode"
)

func countValidWords(sentence string) int {
	ans := 0
	for _, token := range strings.Fields(sentence) {
		if isValid(token) {
			ans++
		}
	}
	return ans
}

func isValid(token string) bool {
	n := len(token)
	if token[0] == '-' || token[n-1] == '-' {
		return false
	}
	hyphenCnt := 0
	for i, c := range token {
		if unicode.IsLower(c) {
			continue
		}
		if unicode.IsNumber(c) {
			return false
		}
		if c == '-' {
			hyphenCnt++
			if hyphenCnt > 1 {
				return false
			}
			if !(unicode.IsLower(rune(token[i-1])) && unicode.IsLower(rune(token[i+1]))) {
				return false
			}
		} else if strings.ContainsRune("!,.", c) {
			if i < n-1 {
				return false
			}
		} else {
			return false
		}
	}
	return true
}
