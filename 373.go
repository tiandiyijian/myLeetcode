package leetcode

import "container/heap"

type PairHeap [][]int

func (h PairHeap) Len() int { return len(h) }

func (h PairHeap) Less(i, j int) bool { return h[i][0]+h[i][1] < h[j][0]+h[j][1] }

func (h PairHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *PairHeap) Push(pair interface{}) {
	*h = append(*h, pair.([]int))
}

func (h *PairHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	ans := [][]int{}
	n1, n2 := len(nums1), len(nums2)
	reverseFlag := false
	if n1 > n2 {
		nums1, nums2 = nums2, nums1
		n1, n2 = n2, n1
		reverseFlag = true
	}
	h := make(PairHeap, n1)
	for i := 0; i < n1; i++ {
		h[i] = []int{nums1[i], nums2[0], i, 0}
	}
	heap.Init(&h)
	for ; k > 0 && len(h) > 0; k-- {
		num1, num2, _, i2 := h[0][0], h[0][1], h[0][2], h[0][3]
		if i2+1 < n2 {
			h[0][1] = nums2[i2+1]
			h[0][3] = i2 + 1
			heap.Fix(&h, 0)
		} else {
			heap.Pop(&h)
		}
		if reverseFlag {
			ans = append(ans, []int{num2, num1})
		} else {
			ans = append(ans, []int{num1, num2})
		}
	}
	return ans
}
