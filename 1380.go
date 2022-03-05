package leetcode

func luckyNumbers(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	min := make([]int, m)
	max := make([]int, n)

	for i := 0; i < m; i++ {
		min[i] = matrix[i][0]
		for j := 0; j < n; j++ {
			if matrix[i][j] < min[i] {
				min[i] = matrix[i][j]
			}
			if matrix[i][j] > max[j] {
				max[j] = matrix[i][j]
			}
		}
	}

	// for i := 0; i < n; i++ {
	//     for j := 0; j < m; j++ {
	//         if matrix[j][i] > max[i] {
	//             max[i] = matrix[j][i]
	//         }
	//     }
	// }

	ans := []int{}
	for i, row := range matrix {
		for j, e := range row {
			if min[i] == e && max[j] == e {
				ans = append(ans, e)
			}
		}
	}

	return ans
}
