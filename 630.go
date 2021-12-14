package leetcode

import (
	"container/heap"
	"sort"
)

type Heap struct {
	sort.IntSlice
}

func (h Heap) Less(i, j int) bool {
	return h.IntSlice[i] > h.IntSlice[j]
}

func (h *Heap) Push(x interface{}) {
	h.IntSlice = append(h.IntSlice, x.(int))
}

func (h *Heap) Pop() interface{} {
	len := len(h.IntSlice)
	x := h.IntSlice[len-1]
	h.IntSlice = h.IntSlice[:len-1]
	return x
}

func scheduleCourse(courses [][]int) int {
	sort.Slice(courses, func(i, j int) bool {
		return courses[i][1] < courses[j][1]
	})
	h := &Heap{}
	day := 1
	for _, c := range courses {
		if day+c[0] <= c[1] {
			day += c[0]
			heap.Push(h, c[0])
		} else if h.Len() > 0 && h.IntSlice[0] > c[0] {
			day += c[0] - h.IntSlice[0]
			h.IntSlice[0] = c[0]
			heap.Fix(h, 0)
		}
	}
	return h.Len()
}
