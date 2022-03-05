package leetcode

func getMaximumGold(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ans := 0

	dx := [4]int{-1, 1, 0, 0}
	dy := [4]int{0, 0, -1, 1}

	var dfs func(int, int, int)
	dfs = func(i, j, gold int) {
		cur := grid[i][j]
		grid[i][j] = 0
		gold += cur
		if gold > ans {
			ans = gold
		}
		for k, x := range dx {
			nx := i + x
			ny := j + dy[k]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] != 0 {
				dfs(nx, ny, gold)
			}
		}
		grid[i][j] = cur
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				dfs(i, j, 0)
			}
		}
	}
	return ans
}
