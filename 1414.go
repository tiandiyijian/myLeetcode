package leetcode

import "sort"

func findMinFibonacciNumbers(k int) int {
	f := []int{1, 1}
	for f[len(f)-1] < k {
		f = append(f, f[len(f)-1]+f[len(f)-2])
	}
	ans := 0
	n := len(f)
	for {
		if k == 0 {
			break
		}
		i := sort.SearchInts(f, k)
		if i == 0 {
			k -= f[0]
		} else {
			if i == n {
				k -= f[i-1]
			} else if f[i] == k {
				k -= f[i]
			} else {
				k -= f[i-1]
			}
		}
		ans++
	}
	return ans
}
