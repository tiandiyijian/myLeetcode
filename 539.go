package leetcode

import "sort"

func findMinDifference(timePoints []string) int {
	sort.Strings(timePoints)
	pre := time2int(timePoints[0])
	first := pre
	ans := 60 * 24
	for i := 1; i < len(timePoints); i++ {
		cur := time2int(timePoints[i])
		if tmp := cur - pre; tmp < ans {
			ans = tmp
		}
		pre = cur
	}
	if tmp := first + 60*24 - pre; tmp < ans {
		return tmp
	}
	return ans
}

func time2int(time string) int {
	// zero := byte('0')
	return 60*int(10*(time[0]-'0')+time[1]-'0') + 10*int(time[3]-'0') + int(time[4]-'0')
}
