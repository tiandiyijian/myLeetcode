package leetcode

import "sort"

type Job struct {
	difficulty int
	profit     int
}

func maxProfitAssignment(difficulty []int, profit []int, worker []int) int {
	n := len(difficulty)
	jobs := make([]Job, n)
	for i, d := range difficulty {
		jobs[i] = Job{d, profit[i]}
	}
	sort.Slice(jobs, func(i, j int) bool {
		return jobs[i].difficulty < jobs[j].difficulty
	})
	ans := 0
	sort.Ints(worker)
	idx := 0
	maxProfit := 0
	for _, skill := range worker {
		for idx < n && jobs[idx].difficulty <= skill {
			if jobs[idx].profit > maxProfit {
				maxProfit = jobs[idx].profit
			}
			idx++
		}
		ans += maxProfit
	}
	return ans
}
