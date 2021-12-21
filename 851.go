package leetcode

func loudAndRich(richer [][]int, quiet []int) []int {
	n := len(quiet)
	edges := make([][]int, n)
	rich := make([]bool, n)
	for _, e := range richer {
		edges[e[1]] = append(edges[e[1]], e[0])
		rich[e[0]] = true
	}

	ans := make([]int, n)
	visit := map[int][2]int{}

	var helper func(x int) (int, int)
	helper = func(x int) (min_q, min_p int) {
		if val, ok := visit[x]; ok {
			return val[0], val[1]
		}
		// visit[x] = [2]int{-1, -1}
		min_q = quiet[x]
		min_p = x
		for _, y := range edges[x] {
			q, p := helper(y)
			if q < min_q {
				min_q = q
				min_p = p
			}
		}
		ans[x] = min_p
		// visit[x][0] = min_q
		// visit[x][1] = min_p
		visit[x] = [2]int{min_q, min_p}
		return
	}

	for p, isRich := range rich {
		if !isRich {
			helper(p)
		}
	}
	return ans
}
