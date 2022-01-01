package leetcode

func construct2DArray(original []int, m int, n int) [][]int {
	if m*n != len(original) {
		return nil
	}
	ans := make([][]int, m)
	for i := 0; i < m; i++ {
		ans[i] = original[i*n : (i+1)*n]
	}
	return ans
}
