package leetcode

func knightProbability(n int, k int, row int, column int) float64 {
	dp := make([][][]float64, k+1)
	dirs := []struct{ x, y int }{
		{1, 2},
		{1, -2},
		{-1, 2},
		{-1, -2},
		{2, 1},
		{2, -1},
		{-2, 1},
		{-2, -1},
	}
	for step := 0; step <= k; step++ {
		dp[step] = make([][]float64, n)
		for i := range dp[step] {
			dp[step][i] = make([]float64, n)
			for j := range dp[step][i] {
				if step == 0 {
					dp[step][i][j] = 1.0
				} else {
					for _, d := range dirs {
						x := d.x + i
						y := d.y + j
						if 0 <= x && x < n && 0 <= y && y < n {
							dp[step][i][j] += dp[step-1][x][y] / 8.0
						}
					}
				}
			}
		}
	}
	return dp[k][row][column]
}
