package leetcode

import (
	"sort"
	"strconv"
	"strings"
)

func largestNumber(nums []int) string {
	n := len(nums)
	strs := make([]string, n)
	zero := 0
	for i, v := range nums {
		strs[i] = strconv.Itoa(v)
		if v == 0 {
			zero++
		}
	}
	if zero == n {
		return "0"
	}
	sort.Slice(strs, func(i, j int) bool {
		lenI := len(strs[i])
		lenJ := len(strs[j])
		p, q := 0, 0
		var a, b byte
		// fmt.Println(strs[i], strs[j], lenI, lenJ)
		for c := 0; c < lenI+lenJ; c++ {
			if p < lenI {
				a = strs[i][p]
			} else {
				a = strs[j][p-lenI]
			}

			if q < lenJ {
				b = strs[j][q]
			} else {
				b = strs[i][q-lenJ]
			}

			if a > b {
				return true
			} else if a < b {
				return false
			}

			p++
			q++
		}
		return true
	})
	// fmt.Println(strs)
	var sb strings.Builder
	for _, v := range strs {
		sb.WriteString(v)
	}
	return sb.String()
}
