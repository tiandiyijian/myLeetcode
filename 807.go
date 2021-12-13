package leetcode

func maxIncreaseKeepingSkyline(grid [][]int) int {
	m := len(grid)
	rowLine := make([]int, m)
	colLine := make([]int, m)
	for i := 0; i < m; i++ {
		rowMax, colMax := 0, 0
		for j := 0; j < m; j++ {
			if grid[i][j] > rowMax {
				rowMax = grid[i][j]
			}
			if grid[j][i] > colMax {
				colMax = grid[j][i]
			}
		}
		rowLine[i] = rowMax
		colLine[i] = colMax
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < m; j++ {
			ans += min(rowLine[i], colLine[j]) - grid[i][j]
		}
	}
	return ans
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
