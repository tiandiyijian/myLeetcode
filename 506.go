package leetcode

import (
	"sort"
	"strconv"
)

func findRelativeRanks(score []int) []string {
	n := len(score)
	idx := make([]int, n)
	ans := make([]string, n)
	for i := 0; i < n; i++ {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool {
		return score[idx[i]] > score[idx[j]]
	})
	for i := 0; i < n; i++ {
		if i == 0 {
			ans[idx[i]] = "Gold Medal"
		} else if i == 1 {
			ans[idx[i]] = "Silver Medal"
		} else if i == 2 {
			ans[idx[i]] = "Bronze Medal"
		} else {
			ans[idx[i]] = strconv.Itoa(i + 1)
		}
	}
	return ans
}
