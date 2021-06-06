package leetcode

func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	// ans := 0
	count := func(str string) (zeros, ones int) {
		for _, c := range str {
			if c == '0' {
				zeros++
			} else if c == '1' {
				ones++
			}
		}
		return
	}
	for _, str := range strs {
		zeros, ones := count(str)
		for j := m; j >= 1; j-- {
			for k := n; k >= 1; k-- {
				if j >= zeros && k >= ones {
					if val := dp[j-zeros][k-ones] + 1; dp[j][k] < val {
						dp[j][k] = val
					}
				}
			}
		}
	}
	return dp[m][n]
}
