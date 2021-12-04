package leetcode

func canConstruct(ransomNote string, magazine string) bool {
	m := len(ransomNote)
	n := len(magazine)
	if m > n {
		return false
	}
	cnt := make([]int, 26)
	for i := 0; i < m; i++ {
		cnt[ransomNote[i]-97]--
	}
	for i := 0; i < n; i++ {
		cnt[magazine[i]-97]++
	}
	for _, v := range cnt {
		if v < 0 {
			return false
		}
	}
	return true
}
