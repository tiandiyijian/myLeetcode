package leetcode

func findJudge(n int, trust [][]int) int {
	in_outDegree := make([]int, n+1)
	for _, t := range trust {
		in_outDegree[t[0]]--
		in_outDegree[t[1]]++
	}
	// ans := -1
	for i := 1; i <= n; i++ {
		if in_outDegree[i] == n-1 {
			return i
		}
	}
	return -1
}
