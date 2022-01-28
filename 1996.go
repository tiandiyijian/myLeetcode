package leetcode

import "sort"

func numberOfWeakCharacters(properties [][]int) int {
	sort.Slice(properties, func(i, j int) bool {
		if properties[i][0] == properties[j][0] {
			return properties[i][1] < properties[j][1]
		}
		return properties[i][0] > properties[j][0]
	})
	// fmt.Println(properties)
	ans := 0
	maxDef := properties[0][1]
	for _, ps := range properties {
		def := ps[1]
		if maxDef > def {
			ans++
		} else {
			maxDef = def
		}
	}
	return ans
}
