package leetcode

func addDigits(num int) int {
	ans := 0
	for {
		ans = 0
		for num > 0 {
			ans += num % 10
			num /= 10
		}
		if ans < 10 {
			return ans
		}
		num = ans
	}
}
