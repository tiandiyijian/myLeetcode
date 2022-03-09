package leetcode

import (
	"math/rand"
	"time"
)

func init() { rand.Seed(time.Now().UnixNano()) }

func sortArray(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	p := partion(nums, 0, len(nums))
	sortArray(nums[:p])
	sortArray(nums[p+1:])
	return nums
}

func partion(nums []int, low, high int) int {
	idx := rand.Int()%(high-low) + low
	nums[low], nums[idx] = nums[idx], nums[low]
	pivot := nums[low]
	i := low
	for j := low; j < high; j++ {
		if nums[j] <= pivot {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	nums[low], nums[i-1] = nums[i-1], nums[low]
	// fmt.Println(nums, i-1)
	return i - 1
}

func sortArray2(nums []int) []int {
	n := len(nums)
	merge := func(i, size int) {
		if i+size >= n {
			return
		}
		tmp := append(make([]int, 0, size), nums[i:i+size]...)
		p1, p2 := 0, i+size
		r1, r2 := size, i+size*2
		for ; p1 < r1 && p2 < r2 && p2 < n; i++ {
			if tmp[p1] <= nums[p2] {
				nums[i] = tmp[p1]
				p1++
			} else {
				nums[i] = nums[p2]
				p2++
			}
		}
		for ; p1 < r1; p1++ {
			nums[i] = tmp[p1]
			i++
		}
	}

	size := 1
	for size < n {
		for i := 0; i < n; i += size * 2 {
			merge(i, size)
		}
		size <<= 1
	}
	return nums
}
