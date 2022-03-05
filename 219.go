package leetcode

func containsNearbyDuplicate(nums []int, k int) bool {
	mp := map[int]int{}
	n := len(nums)
	for i := 0; i < n; i++ {
		if _, ok := mp[nums[i]]; ok {
			return true
		}
		mp[nums[i]] = i
		if j := i - k; j >= 0 {
			if mp[nums[j]] == j {
				delete(mp, nums[j])
			}
		}
	}
	return false
}
