package leetcode

/*
 * @lc app=leetcode.cn id=477 lang=golang
 *
 * [477] 汉明距离总和
 */

// @lc code=start
func totalHammingDistance(nums []int) int {
	ans := 0
	n := len(nums)
	for i := 0; i < 30; i++ {
		c := 0
		for _, num := range nums {
			c += num >> i & 1
		}
		ans += c * (n - c) // 在每一位上的总距离为1的个数乘0的个数
	}
	return ans
}

// @lc code=end
