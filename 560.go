package leetcode

func subarraySum(nums []int, k int) (ans int) {
	mp := map[int]int{0: 1}
	sum := 0
	for _, val := range nums {
		sum += val
		if val, ok := mp[sum-k]; ok {
			ans += val
		}
		// ans += mp[sum - k]
		mp[sum]++
	}
	return
}
