package leetcode

func maxCount(m int, n int, ops [][]int) int {
	min_row, min_col := m, n
	for _, op := range ops {
		row, col := op[0], op[1]
		if row < min_row {
			min_row = row
		}
		if col < min_col {
			min_col = col
		}
	}
	return min_row * min_col
}
