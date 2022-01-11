package leetcode

import "strings"

func findOcurrences(text string, first string, second string) []string {
	ans := []string{}
	words := strings.Split(text, " ")
	n := len(words)
	if n < 3 {
		return ans
	}
	for i := 0; i < n-2; i++ {
		if words[i] == first && words[i+1] == second {
			ans = append(ans, words[i+2])
		}
	}
	return ans
}
