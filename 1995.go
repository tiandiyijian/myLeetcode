package leetcode

func countQuadruplets(nums []int) int {
	n := len(nums)
	ans := 0
	cnt := map[int]int{}
	for c := n - 2; c > 1; c-- {
		for d := c + 1; d < n; d++ {
			cnt[nums[d]-nums[c]]++
		}
		b := c - 1
		for a := 0; a < b; a++ {
			ans += cnt[nums[a]+nums[b]]
		}
	}
	return ans
}
