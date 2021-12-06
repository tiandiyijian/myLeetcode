package leetcode

func truncateSentence(s string, k int) string {
	sep := byte(' ')
	i := 0
	for ; i < len(s); i++ {
		if s[i] == sep {
			k--
			if k == 0 {
				break
			}
		}
	}
	return s[:i]
}
