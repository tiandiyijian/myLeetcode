package leetcode

type point [2]int

func highestPeak(isWater [][]int) [][]int {
	m, n := len(isWater), len(isWater[0])
	ans := make([][]int, m)
	q := []point{}
	for i := range ans {
		ans[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if isWater[i][j] == 1 {
				q = append(q, point{i, j})
			}
		}
	}
	visit := func(i, j int) bool {
		return isWater[i][j] == 1 || ans[i][j] > 0
	}
	dx := []int{0, 0, -1, 1}
	dy := []int{-1, 1, 0, 0}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		x, y := p[0], p[1]
		for i := range dx {
			nx := x + dx[i]
			ny := y + dy[i]
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !visit(nx, ny) {
				ans[nx][ny] = ans[x][y] + 1
				q = append(q, point{nx, ny})
			}
		}
	}
	return ans
}
