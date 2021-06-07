package main

import "fmt"

func findTargetSumWays(nums []int, target int) int {
	mp := map[int]int{nums[0]: 1}
	if nums[0] != 0 {
		mp[-nums[0]] = 1
	} else {
		mp[0] = 2
	}
	for _, num := range nums[1:] {
		tmp := map[int]int{}
		for key := range mp {
			if _, ok := tmp[key-num]; ok {
				tmp[key-num] += mp[key]
			} else {
				tmp[key-num] = mp[key]
			}

			if _, ok := tmp[key+num]; ok {
				tmp[key+num] += mp[key]
			} else {
				tmp[key+num] = mp[key]
			}
		}
		mp = tmp
	}
	return mp[target]
}

func main() {
	nums := []int{0, 0, 0, 1}
	fmt.Println(findTargetSumWays(nums, 1))
}
