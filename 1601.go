package leetcode

func maximumRequests(n int, requests [][]int) int {
	m := len(requests)
	move := make([]int, n)
	// dst := make([]int, n)

	var helper func(int, int) int
	helper = func(i, r int) int {
		if i == m {
			for _, v := range move {
				if v != 0 {
					return 0
				}
			}
			return r
		}
		// choose
		move[requests[i][0]]++
		move[requests[i][1]]--
		a := helper(i+1, r+1)
		// not choose
		move[requests[i][0]]--
		move[requests[i][1]]++
		return max(a, helper(i+1, r))
	}
	return helper(0, 0)
}

func maximumRequests2(n int, requests [][]int) int {
	m := len(requests)
	ans := 0
	move := make([]int, n)

	var helper func(int, int)
	helper = func(i, r int) {
		if i == m {
			for _, v := range move {
				if v != 0 {
					return
				}
			}
			ans = max(ans, r)
			return
		}
		if r+m-i <= ans {
			return
		}
		// choose
		move[requests[i][0]]++
		move[requests[i][1]]--
		helper(i+1, r+1)
		// not choose
		move[requests[i][0]]--
		move[requests[i][1]]++
		helper(i+1, r)
	}

	helper(0, 0)
	return ans
}

func maximumRequests3(n int, requests [][]int) int {
	m := len(requests)
	ans := 0
	move := make([]int, n)
	zero := n
	// 其实可以记录move中0的个数直接判断是否合法

	var helper func(int, int)
	helper = func(i, r int) {
		if i == m {
			if zero != n {
				return
			}
			ans = max(ans, r)
			return
		}
		if r+m-i <= ans {
			return
		}
		// choose
		z := zero
		x, y := requests[i][0], requests[i][1]
		if move[x] == 0 {
			zero--
		}
		move[x]++
		if move[x] == 0 {
			zero++
		}
		if move[y] == 0 {
			zero--
		}
		move[y]--
		if move[y] == 0 {
			zero++
		}
		helper(i+1, r+1)

		// not choose
		move[x]--
		move[y]++
		zero = z
		helper(i+1, r)
	}

	helper(0, 0)
	return ans
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
