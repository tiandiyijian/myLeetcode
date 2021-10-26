package leetcode

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	mp := map[int]int{}
	for idx, val := range nums1 {
		mp[val] = idx
	}
	s := []int{}
	ans := make([]int, len(nums1))
	for i := len(nums2) - 1; i >= 0; i-- {
		for len(s) > 0 && s[len(s)-1] <= nums2[i] {
			s = s[:len(s)-1]
		}
		if idx, ok := mp[nums2[i]]; ok {
			if len(s) > 0 {
				ans[idx] = s[len(s)-1]
			} else {
				ans[idx] = -1
			}
		}
		s = append(s, nums2[i])
	}
	return ans
}
