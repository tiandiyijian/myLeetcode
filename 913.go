package leetcode

func catMouseGame(graph [][]int) int {
	n := len(graph)
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, 2*n)
		}
	}
	var dfs func(int, int, int) int
	dfs = func(mouse, cat, turn int) int {
		if dp[mouse][cat][turn] > 0 {
			return dp[mouse][cat][turn]
		}
		if mouse == 0 {
			dp[mouse][cat][turn] = 1
			return 1
		}
		if mouse == cat {
			dp[mouse][cat][turn] = 2
			return 2
		}
		if turn+1 == n<<1 {
			// 记平局为3
			dp[mouse][cat][turn] = 3
			return 3
		}
		ans := 2
		if turn&1 == 0 {
			for _, next := range graph[mouse] {
				tmp := dfs(next, cat, turn+1)
				if tmp == 3 {
					ans = 3
				}
				if tmp == 1 {
					ans = 1
					break
				}
			}
		} else {
			ans = 1
			for _, next := range graph[cat] {
				if next == 0 {
					continue
				}
				tmp := dfs(mouse, next, turn+1)
				if tmp == 3 {
					ans = 3
				}
				if tmp == 2 {
					ans = 2
					break
				}
			}
		}
		dp[mouse][cat][turn] = ans
		return ans
	}
	ans := dfs(1, 2, 0)
	if ans == 3 {
		return 0
	}
	return ans
}
