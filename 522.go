package leetcode

import "sort"

func findLUSlength(strs []string) int {
	// 答案一定是字符串列表中的字符串而不是某个字符串的子序列
	// 反证法:
	// 假如某个字符串的子序列是特殊序列
	// 那么如果把这个子序列扩充成原字符串
	// 它依然是特殊序列而且更长
	sort.Slice(strs, func(i, j int) bool {
		if len(strs[i]) == len(strs[j]) {
			return strs[i] < strs[j]
		}
		return len(strs[i]) > len(strs[j])
	})

	n := len(strs)
	for i := 0; i < n; i++ {
		if i > 0 && strs[i] == strs[i-1] {
			continue
		}
		lenI := len(strs[i])
		flag := false
		for j := 0; j < n && len(strs[j]) >= lenI; j++ {
			if j == i {
				continue
			}
			if isSubsequence(strs[i], strs[j]) {
				flag = true
				break
			}
		}
		if !flag {
			return lenI
		}
	}
	return -1
}

func isSubsequence(a, b string) bool {
	i := 0
	lenA := len(a)
	for j := 0; j < len(b) && i < lenA; j++ {
		if b[j] == a[i] {
			i++
		}
	}
	return i == lenA
}
