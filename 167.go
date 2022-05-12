package leetcode

func twoSum(numbers []int, target int) []int {
	n := len(numbers)
	r := n - 1
	for l := 0; l < n-1; l++ {
		r = BSearch(numbers, target-numbers[l], l+1, r)
		if numbers[l]+numbers[r] == target {
			return []int{l, r}
		}
	}
	return []int{}
}

func BSearch(numbers []int, target, l, r int) int {
	// fmt.Println(numbers, target, l, r)
	if numbers[r] <= target {
		return r
	}
	if numbers[l] >= target {
		return l
	}
	for l <= r {
		mid := (l + r) >> 1
		if numbers[mid] == target {
			for mid > l && numbers[mid-1] == target {
				mid--
			}
			return mid
		} else if numbers[mid] > target {
			r = mid - 1
		} else {
			if numbers[mid+1] > target {
				return mid
			}
			l = mid + 1
		}
	}
	// fmt.Println(numbers, target, l, r)
	return l
}

// func main() {
// 	numbers := []int{2, 7, 11, 15}
// 	target := 9
// 	fmt.Println(BSearch(numbers, 7, 1, 3))
// 	fmt.Println(twoSum(numbers, target))
// }
