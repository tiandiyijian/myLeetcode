package leetcode

func nthUglyNumber(n int) int {
	dp := make([]int, n+1)
	dp[1] = 1
	p2, p3, p5 := 1, 1, 1
	for i := 2; i <= n; i++ {
		num2, num3, num5 := dp[p2]*2, dp[p3]*3, dp[p5]*5
		min := num2
		if num3 < min {
			min = num3
		}
		if num5 < min {
			min = num5
		}
		dp[i] = min
		if dp[i] == num2 {
			p2++
		}
		if dp[i] == num3 {
			p3++
		}
		if dp[i] == num5 {
			p5++
		}
	}
	// fmt.Println(dp)
	return dp[n]
}
