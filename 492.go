package leetcode

import "math"

func constructRectangle(area int) []int {
	root := math.Sqrt(float64(area))
	w := int(root)
	for area%w != 0 {
		w--
	}
	return []int{area / w, w}
}
