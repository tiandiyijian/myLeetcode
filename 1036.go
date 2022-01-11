package main

import "fmt"

var (
	dx = [4]int{0, 0, -1, 1}
	dy = [4]int{1, -1, 0, 0}
)

const MAX = 1e6

func isEscapePossible(blocked [][]int, source []int, target []int) bool {
	n := len(blocked)
	max_area := n * (n - 1) / 2
	block := map[[2]int]struct{}{}
	for i := 0; i < n; i++ {
		block[[2]int{blocked[i][0], blocked[i][1]}] = struct{}{}
	}
	if bfs(source[0], source[1], target[0], target[1], max_area, block) && bfs(target[0], target[1], source[0], source[1], max_area, block) {
		return true
	}
	return false
}

func bfs(x, y, tx, ty, max_area int, block map[[2]int]struct{}) bool {
	visit := map[[2]int]struct{}{}
	q := [][2]int{{x, y}}
	visit[[2]int{x, y}] = struct{}{}
	for len(q) > 0 {
		current_size := len(q)
		new_q := [][2]int{}
		for i := 0; i < current_size; i++ {
			a, b := q[i][0], q[i][1]
			for j := 0; j < 4; j++ {
				na, nb := a+dx[j], b+dy[j]
				if 0 <= na && na < MAX && 0 <= nb && nb < MAX {
					point := [2]int{na, nb}
					// fmt.Println(point)
					if _, ok := block[point]; ok {
						continue
					}
					if _, ok := visit[point]; !ok {
						if na == tx && nb == ty {
							return true
						}
						visit[point] = struct{}{}
						new_q = append(new_q, point)
					}
				}
			}
			if len(visit) > max_area {
				return true
			}
		}
		q = new_q
	}
	return false
}

func main() {
	blocked := [][]int{
		{0, 1},
		{1, 0},
	}
	source := []int{0, 0}
	target := []int{0, 2}
	fmt.Println(isEscapePossible(blocked, source, target))
}
