package leetcode

func countKDifference(nums []int, k int) int {
	cnter := map[int]int{}
	for _, n := range nums {
		cnter[n]++
	}
	ans := 0
	for n, c := range cnter {
		ans += c * cnter[n+k]
	}
	return ans
}
