package leetcode

type TopVotedCandidate struct {
	times []int
	max   []int
}

func Constructor(persons []int, times []int) TopVotedCandidate {
	t := TopVotedCandidate{
		times: times,
	}
	max_p, max_vote := -1, -1
	person_votes := map[int]int{}
	max := []int{}
	for _, p := range persons {
		person_votes[p]++
		if tmp := person_votes[p]; tmp >= max_vote {
			max_vote = tmp
			max_p = p
		}
		max = append(max, max_p)
	}
	t.max = max
	return t
}

func (this *TopVotedCandidate) Q(t int) int {
	idx := binSearch(this.times, t)
	return this.max[idx]
}
func binSearch(arr []int, target int) int {
	low, high := 0, len(arr)-1
	if target >= arr[high] {
		return high
	}
	if target < arr[low] {
		return -1
	}
	for high >= low {
		// fmt.Println(low, high)
		mid := (high-low)>>1 + low
		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	// arr[low]始终<=target
	// 当low大于high时说明low == high时仍不符合条件并且arr[low]<target即arr[mid]<target
	// 所以才把low++
	return low - 1
}

// func main() {
// 	persons := []int{0, 1, 1, 0, 0, 1, 0}
// 	times := []int{0, 5, 10, 15, 20, 25, 30}
// 	// fmt.Println(binSearch(times, 8))
// 	t := Constructor(persons, times)
// 	fmt.Println(t.max)
// 	fmt.Println(t.Q(78))
// }
