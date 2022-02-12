package leetcode

func numEnclaves(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dxs := [4]int{0, 0, -1, 1}
	dys := [4]int{-1, 1, 0, 0}
	bfs := func(i, j int) int {
		flag := false
		cnt := 0
		q := []int{i*n + j}
		grid[i][j] = -1
		cnt++
		if i == 0 || i == m-1 || j == 0 || j == n-1 {
			flag = true
		}
		for len(q) > 0 {
			x, y := q[0]/n, q[0]%n
			q = q[1:]
			for i, dx := range dxs {
				dy := dys[i]
				nx, ny := x+dx, y+dy
				if 0 <= nx && nx < m && 0 <= ny && ny < n && grid[nx][ny] == 1 {
					cnt++
					grid[nx][ny] = -1
					q = append(q, nx*n+ny)
					if nx == 0 || nx == m-1 || ny == 0 || ny == n-1 {
						flag = true
					}
				}
			}
		}
		if !flag {
			return cnt
		}
		return 0
	}

	ans := 0
	for i, row := range grid {
		for j := range row {
			if grid[i][j] == 1 {
				ans += bfs(i, j)
			}
		}
	}
	return ans
}
