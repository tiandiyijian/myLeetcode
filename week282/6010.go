package week282

import "fmt"

func minimumTime(time []int, totalTrips int) int64 {
	n := len(time)
	if n == 1 {
		return int64(totalTrips * time[0])
	}

	minT := 100000000
	for _, t := range time {
		if t < minT {
			minT = t
		}
	}
	maxTime := int64(minT) * int64(totalTrips)
	fmt.Println(maxTime)
	return Search(maxTime+1, func(i int64) bool {
		cnt := int64(0)
		for _, t := range time {
			cnt += i / int64(t)
			if cnt >= int64(totalTrips) {
				return true
			}
		}
		return false
	})
}

func Search(n int64, f func(int64) bool) int64 {
	// Define f(-1) == false and f(n) == true.
	// Invariant: f(i-1) == false, f(j) == true.
	i, j := int64(0), n
	for i < j {
		h := int64(uint64(i+j) >> 1) // avoid overflow when computing h
		// i ≤ h < j
		if !f(h) {
			i = h + 1 // preserves f(i-1) == false
		} else {
			j = h // preserves f(j) == true
		}
	}
	// i == j, f(i-1) == false, and f(j) (= f(i)) == true  =>  answer is i.
	return i
}
