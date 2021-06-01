package leetcode

func canEat(candiesCount []int, queries [][]int) []bool {
	n := len(candiesCount)
	preSum := make([]int, n+1)
	for i := range candiesCount {
		preSum[i+1] = preSum[i] + candiesCount[i]
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		candyType, day, cap := q[0], q[1], q[2]
		max := (day + 1) * cap
		min := day
		if max <= preSum[candyType] || min >= preSum[candyType+1] {
			ans[i] = false
		} else {
			ans[i] = true
		}
	}
	return ans
}
