package leetcode

import (
	"container/heap"
	"sort"
)

type minHeap struct {
	sort.IntSlice
}

func (h *minHeap) Push(x interface{}) {
	h.IntSlice = append(h.IntSlice, x.(int))
}

func (h *minHeap) Pop() interface{} {
	old := h.IntSlice
	n := len(old)
	x := h.IntSlice[n-1]
	h.IntSlice = old[:n-1]
	return x
}

// type maxHeap struct {
// 	sort.IntSlice
// }

// func (h *maxHeap) Less(i, j int) bool {
// 	return h.IntSlice[i] > h.IntSlice[j]
// }

// func (h *maxHeap) Push(x interface{}) {
// 	h.IntSlice = append(h.IntSlice, x.(int))
// }

// func (h *maxHeap) Pop() interface{} {
// 	old := h.IntSlice
// 	n := len(old)
// 	x := h.IntSlice[n-1]
// 	h.IntSlice = old[:n-1]
// 	return x
// }

type MedianFinder struct {
	minHeap *minHeap
	maxHeap *minHeap
}

func Constructor() MedianFinder {
	return MedianFinder{
		minHeap: new(minHeap),
		maxHeap: new(minHeap),
	}
}

func (this *MedianFinder) AddNum(num int) {
	if this.minHeap.Len() == 0 {
		heap.Push(this.minHeap, num)
		return
	}
	if num >= this.minHeap.IntSlice[0] {
		heap.Push(this.minHeap, num)
		if this.minHeap.Len() > this.maxHeap.Len()+1 {
			heap.Push(this.maxHeap, -heap.Pop(this.minHeap).(int))
		}
	} else {
		heap.Push(this.maxHeap, -num)
		if this.maxHeap.Len() > this.minHeap.Len() {
			heap.Push(this.minHeap, -heap.Pop(this.maxHeap).(int))
		}
	}
	// fmt.Println(this.maxHeap, this.minHeap)
}

func (this *MedianFinder) FindMedian() float64 {
	if this.maxHeap.Len() == this.minHeap.Len() {
		return (float64(-this.maxHeap.IntSlice[0]) + float64(this.minHeap.IntSlice[0])) / 2
	} else {
		return float64(this.minHeap.IntSlice[0])
	}
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
