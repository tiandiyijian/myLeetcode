package leetcode

func goodDaysToRobBank(security []int, time int) []int {
	n := len(security)
	ascending := make([]int, n)
	descending := make([]int, n)

	ascending[0] = 1
	descending[n-1] = 1
	for i := 1; i < n; i++ {
		if security[i] <= security[i-1] {
			ascending[i] = ascending[i-1] + 1
		} else {
			ascending[i] = 1
		}

		if security[n-i-1] <= security[n-i] {
			descending[n-i-1] = descending[n-i] + 1
		} else {
			descending[n-i-1] = 1
		}
	}

	ans := make([]int, 0)
	for i := 0; i < n; i++ {
		if ascending[i] > time && descending[i] > time {
			ans = append(ans, i)
		}
	}
	return ans
}
