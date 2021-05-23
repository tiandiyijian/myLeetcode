package leetcode

/*
 * @lc app=leetcode.cn id=1442 lang=golang
 *
 * [1442] 形成两个异或相等数组的三元组数目
 */
// @lc code=start
func countTriplets(arr []int) int {
	cnt := make(map[int]int)
	total := map[int]int{}
	s := 0
	ans := 0
	for k, val := range arr {
		if m, has := cnt[s^val]; has {
			ans += m*k - total[s^val]
		}
		cnt[s]++
		total[s] += k
		s ^= val
	}
	return ans
}

// @lc code=end
