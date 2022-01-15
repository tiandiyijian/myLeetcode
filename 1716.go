package leetcode

func totalMoney(n int) int {
	oneWeek := 28
	week := n / 7
	day := n % 7
	return oneWeek*week + day*(day+1)/2 + 7*(week-1)*week/2 + day*week
}
