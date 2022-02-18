package leetcode

func findCenter(edges [][]int) int {
	n := len(edges) + 1
	degree := make([]int, n+1)
	for _, e := range edges {
		degree[e[0]]++
		degree[e[1]]++
	}
	for i, d := range degree {
		if d == n-1 {
			return i
		}
	}
	return 0
}
