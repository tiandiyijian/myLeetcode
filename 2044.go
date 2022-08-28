package leetcode

func countMaxOrSubsets(nums []int) int {
	n := len(nums)

	max := 0
	for _, v := range nums {
		max |= v
	}

	var dfs func(int, int) int
	dfs = func(i, state int) int {
		if i == n {
			if state == max {
				return 1
			}
			return 0
		}

		if state == max {
			return 1 << (n - i)
		}

		return dfs(i+1, state|nums[i]) + dfs(i+1, state)
	}

	return dfs(0, 0)
}
