package leetcode

func longestSubsequence(arr []int, difference int) int {
	ans := 1
	// dp[i] = dp[k] + 1 where arr[i] - difference = arr[k]
	pre := map[int]int{}
	for _, num := range arr {
		pre[num] = pre[num-difference] + 1
		if pre[num] > ans {
			ans = pre[num]
		}
	}
	return ans
}
