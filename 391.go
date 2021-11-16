package leetcode

import "math"

func isRectangleCover(rectangles [][]int) bool {
	area := 0
	left, bottom := math.MaxInt64, math.MaxInt64
	right, top := math.MinInt64, math.MinInt64
	cnt := map[[2]int]int{}
	for _, r := range rectangles {
		x, y, a, b := r[0], r[1], r[2], r[3]
		area += (a - x) * (b - y)
		left = min(left, x)
		bottom = min(bottom, y)
		right = max(right, a)
		top = max(top, b)

		cnt[[2]int{x, y}] += 1
		cnt[[2]int{x, b}] += 1
		cnt[[2]int{a, y}] += 1
		cnt[[2]int{a, b}] += 1
	}
	if area != (right-left)*(top-bottom) {
		return false
	}

	if cnt[[2]int{left, bottom}] != 1 {
		return false
	} else {
		delete(cnt, [2]int{left, bottom})
	}

	if cnt[[2]int{left, top}] != 1 {
		return false
	} else {
		delete(cnt, [2]int{left, top})
	}

	if cnt[[2]int{right, bottom}] != 1 {
		return false
	} else {
		delete(cnt, [2]int{right, bottom})
	}

	if cnt[[2]int{right, top}] != 1 {
		return false
	} else {
		delete(cnt, [2]int{right, top})
	}
	for _, val := range cnt {
		if !(val == 2 || val == 4) {
			return false
		}
	}
	return true
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
