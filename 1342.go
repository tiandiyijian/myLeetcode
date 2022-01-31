package leetcode

func numberOfSteps(num int) int {
	ans := 0
	for ; num > 0; num >>= 1 {
		ans += num & 1
		if num > 0 {
			ans++
		}
	}
	return ans
}
