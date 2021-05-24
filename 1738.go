package leetcode

import "sort"

func kthLargestValue(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	numbers := make([]int, m*n)
	pre := make([][]int, m)
	for i := range pre {
		pre[i] = make([]int, n)
		if i > 0 {
			pre[i][0] = matrix[i][0] ^ pre[i-1][0]
		} else {
			pre[i][0] = matrix[i][0]
		}
		numbers = append(numbers, pre[i][0])
	}
	for i := 1; i < n; i++ {
		pre[0][i] = matrix[0][i] ^ pre[0][i-1]
		numbers = append(numbers, pre[0][i])
	}
	// fmt.Println(pre)
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			pre[i][j] = pre[i-1][j-1] ^ pre[i][j-1] ^ pre[i-1][j] ^ matrix[i][j]
			// fmt.Println(pre[i][j])
			numbers = append(numbers, pre[i][j])
		}
	}
	// fmt.Println(numbers)
	sort.Sort(sort.Reverse(sort.IntSlice(numbers)))
	return numbers[k-1]
}
