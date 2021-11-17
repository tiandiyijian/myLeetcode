package leetcode

func maxProduct(words []string) int {
	mp := map[int]int{}
	for _, word := range words {
		bits := 0
		for _, c := range word {
			bits |= 1 << (c - 97)
		}
		if mp[bits] < len(word) {
			mp[bits] = len(word)
		}
	}
	ans := 0
	for i, len1 := range mp {
		for j, len2 := range mp {
			if i&j == 0 && len1*len2 > ans {
				ans = len1 * len2
			}
		}
	}
	return ans
}
