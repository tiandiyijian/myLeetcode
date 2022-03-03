package leetcode

import "sort"

func search(nums []int, target int) int {
	// 耍赖写法，先找出旋转点的下标再判断用前半段二分还是后半段二分
	// 旋转点的特征是那个点后面的所有点的值都小于第一个点的值，所以也可以用二分来找到
	// 用sort.Search也太方便了
	Bsearch := func(low, high int) int {
		for low <= high {
			mid := (low + high) / 2
			if nums[mid] == target {
				return mid
			} else if nums[mid] > target {
				high = mid - 1
			} else {
				low = low + 1
			}
		}
		return -1
	}

	n := len(nums)
	if nums[n-1] >= nums[0] {
		return Bsearch(0, n-1)
	}
	k := sort.Search(n-1, func(i int) bool {
		return nums[i] < nums[0]
	})
	// fmt.Println(k)
	if target < nums[k] {
		return -1
	}
	if target <= nums[n-1] {
		return Bsearch(k, n-1)
	}
	if target > nums[k-1] {
		return -1
	}
	return Bsearch(0, k-1)
}
