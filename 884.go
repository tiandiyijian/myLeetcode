package leetcode

import "strings"

func uncommonFromSentences(s1 string, s2 string) []string {
	l1 := strings.Fields(s1)
	l2 := strings.Fields(s2)
	l1 = append(l1, l2...)
	cnter := map[string]int{}
	for _, w := range l1 {
		cnter[w]++
	}
	ans := []string{}
	for w, cnt := range cnter {
		if cnt == 1 {
			ans = append(ans, w)
		}
	}
	return ans
}
