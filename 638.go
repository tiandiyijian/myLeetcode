package leetcode

func shoppingOffers(price []int, special [][]int, needs []int) int {
	n := len(needs)
	filterSpecial := [][]int{}
	for _, s := range special {
		count, totalPrice := 0, 0
		for i, c := range s[:n] {
			count += c
			totalPrice += c * price[i]
		}
		if count > 0 && totalPrice > s[n] {
			filterSpecial = append(filterSpecial, s)
		}
	}

	cache := map[string]int{}
	var dfs func([]byte) int
	dfs = func(curNeeds []byte) (minPrice int) {
		// []byte 可以直接转为string, 而[]int不行
		if res, has := cache[string(curNeeds)]; has {
			return res
		}
		for i, p := range price {
			minPrice += p * int(curNeeds[i])
		}
		nextNeeds := make([]byte, n)
	outer:
		for _, s := range filterSpecial {
			for i, need := range curNeeds {
				if need < byte(s[i]) {
					continue outer
				}
				nextNeeds[i] = need - byte(s[i])
			}
			minPrice = min(minPrice, dfs(nextNeeds)+s[n])
		}
		return
	}

	curNeeds := make([]byte, n)
	for i, n := range needs {
		curNeeds[i] = byte(n)
	}
	return dfs(curNeeds)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
