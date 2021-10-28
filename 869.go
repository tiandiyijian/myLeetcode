package leetcode

func reorderedPowerOf2(n int) bool {
	return all_count[countDigits(n)]
}

func countDigits(n int) (ans [10]int) {
	for n > 0 {
		ans[n%10] += 1
		n /= 10
	}
	return
}

var all_count = map[[10]int]bool{}

func init() {
	for i := 0; i < 32; i++ {
		all_count[countDigits(1<<i)] = true
	}
}
