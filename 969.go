package leetcode

func pancakeSort(arr []int) []int {
	n := len(arr)
	ans := []int{}
	for i := n; i > 0; i-- {
		idx := 0
		for j, v := range arr {
			if v == i {
				idx = j
				break
			}
		}
		if idx == i-1 {
			continue
		}
		ans = append(ans, idx+1)
		for p, q := 0, idx; p < q; p++ {
			arr[p], arr[q] = arr[q], arr[p]
			q--
		}
		ans = append(ans, i)
		for p, q := 0, i-1; p < q; p++ {
			arr[p], arr[q] = arr[q], arr[p]
			q--
		}
	}
	return ans
}
