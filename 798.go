package leetcode

func bestRotation(nums []int) int {
	// 暴力解法
	l := len(nums)
	ans := 0
	max_score := 0
	for k := 0; k < l; k++ {
		score := 0
		for i := 0; i < l; i++ {
			if i >= nums[(i+k)%l] {
				score++
			}
		}
		if score > max_score {
			max_score = score
			ans = k
		}
	}
	return ans
}

func bestRotation2(nums []int) int {
	// 差分
	l := len(nums)
	diff := make([]int, l+1)
	for i, v := range nums {
		if i >= v {
			// k的范围为[0, i-v]和[i+1,i+l-v]即[i+1,l)
			diff[0]++
			diff[i-v+1]--
			diff[i+1]++
			diff[l]--
		} else {
			// k的范围为[i+1,i+l-v]
			diff[i+1]++
			diff[i+l-v+1]--
		}
	}
	// fmt.Println(diff)
	ans := 0
	max_score := 0
	score := 0
	for k, v := range diff {
		score += v
		if score > max_score {
			score = max_score
			ans = k
		}
	}
	return ans
}
