package leetcode

func countGoodRectangles(rectangles [][]int) int {
	maxLen := 0
	for _, r := range rectangles {
		if tmp := min(r[0], r[1]); tmp > maxLen {
			maxLen = tmp
		}
	}
	cnt := 0
	for _, r := range rectangles {
		if min(r[0], r[1]) >= maxLen {
			cnt++
		}
	}
	return cnt
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
