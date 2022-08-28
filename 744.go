package leetcode

import "sort"

func nextGreatestLetter(letters []byte, target byte) byte {
	n := len(letters)

	if letters[n-1] <= target {
		return letters[0]
	}

	return letters[sort.Search(n, func(i int) bool {
		return letters[i] > target
	})]
}
