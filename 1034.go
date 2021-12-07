package leetcode

func colorBorder(grid [][]int, row int, col int, color int) [][]int {
	if grid[row][col] == color {
		return grid
	}
	m, n := len(grid), len(grid[0])
	oldColor := grid[row][col]
	q := [][2]int{{row, col}}
	visit := map[int]struct{}{}
	visit[row*n+col] = struct{}{}
	border := [][2]int{}
	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		x, y := q[0][0], q[0][1]
		// fmt.Println(x, y)
		q = q[1:]
		isBorder := false
		for _, d := range directions {
			nx, ny := x+d[0], y+d[1]
			if 0 <= nx && nx < m && 0 <= ny && ny < n {
				if grid[nx][ny] != oldColor {
					isBorder = true
				} else {
					if _, ok := visit[nx*n+ny]; !ok {
						visit[nx*n+ny] = struct{}{}
						q = append(q, [2]int{nx, ny})
						// fmt.Println(nx, ny, visit)
					}
				}
			}
		}
		if !isBorder && (x == 0 || x == m-1 || y == 0 || y == n-1) {
			isBorder = true
		}
		if isBorder {
			border = append(border, [2]int{x, y})
		}
	}
	for _, p := range border {
		grid[p[0]][p[1]] = color
	}
	// fmt.Println(cnt)
	return grid
}

// func main() {
// 	grid := [][]int{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}
// 	fmt.Println(colorBorder(grid, 0, 0, 3))
// }
