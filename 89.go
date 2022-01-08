package leetcode

func grayCode(n int) []int {
	ans := make([]int, 1<<n)
	for i := 0; i < n; i++ {
		adder := 1 << i
		for j := 0; j < adder; j++ {
			ans[adder+j] = adder + ans[adder-j-1]
		}
	}
	return ans
}
