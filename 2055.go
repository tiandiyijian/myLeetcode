package leetcode

func platesBetweenCandles(s string, queries [][]int) []int {
	n := len(s)
	pre := make([]int, n)
	next_plate := make([]int, n)
	cur_plate := n
	plates := 0
	for i := 0; i < n; i++ {
		if s[i] == '*' {
			plates++
			if i > 0 {
				pre[i] = pre[i-1]
			}
		} else {
			pre[i] = plates
		}

		j := n - i - 1
		if s[j] == '|' {
			cur_plate = j
		}
		next_plate[j] = cur_plate
	}
	// fmt.Println(pre)
	lenQ := len(queries)
	ans := make([]int, lenQ)
	for i := 0; i < lenQ; i++ {
		l, r := queries[i][0], queries[i][1]
		// for l < r && s[l] != '|' {
		// 	l++
		// }
		l = next_plate[l]
		if l >= r {
			ans[i] = 0
		} else {
			ans[i] = pre[r] - pre[l]
		}
	}
	return ans
}
