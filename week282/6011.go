package week282

import "math"

func minimumFinishTime(tires [][]int, changeTime int, numLaps int) int {
	// 不可能连续很多圈使用同一个轮胎，假设最多连续使用20圈
	K := 20
	best := [21]int{}
	for i := range best {
		best[i] = math.MaxInt32
	}
	for _, t := range tires {
		f, r := t[0], t[1]
		last, tot := f, f
		for i := 1; i < 21; i++ {
			if tot >= math.MaxInt32 {
				break
			}
			if tot < best[i] {
				best[i] = tot
			}
			last *= r
			tot += last
		}
	}
	// fmt.Println(best)
	dp := make([]int, numLaps+1)
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0
	for i := range dp {
		start := 0
		if i-K > 0 {
			start = i - K
		}
		for j := start; j < i; j++ {
			if tmp := dp[j] + changeTime + best[i-j]; tmp < dp[i] {
				dp[i] = tmp
			}
		}
	}
	// fmt.Println(dp)
	// 第一圈不需要加换轮胎时间
	return dp[numLaps] - changeTime
}
