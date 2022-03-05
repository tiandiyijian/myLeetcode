package leetcode

func gridIllumination(n int, lamps [][]int, queries [][]int) []int {
	points := map[[2]int]bool{}
	row, col, diagonal, antiDiagonal := map[int]int{}, map[int]int{}, map[int]int{}, map[int]int{}
	for _, lamp := range lamps {
		x, y := lamp[0], lamp[1]
		p := [2]int{x, y}
		if points[p] {
			continue
		}
		points[p] = true
		row[x]++
		col[y]++
		diagonal[y-x]++
		antiDiagonal[y+x]++
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		// fmt.Println(points)
		// fmt.Println(row, col, diagonal, antiDiagonal)
		x, y := q[0], q[1]
		if row[x] > 0 || col[y] > 0 || diagonal[y-x] > 0 || antiDiagonal[y+x] > 0 {
			ans[i] = 1
		}
		for r := x - 1; r <= x+1; r++ {
			for c := y - 1; c <= y+1; c++ {
				if 0 <= r && r < n && 0 <= c && c < n {
					p := [2]int{r, c}
					if points[p] {
						points[p] = false
						row[r]--
						col[c]--
						diagonal[c-r]--
						antiDiagonal[c+r]--
					}
				}
			}
		}
	}
	return ans
}
