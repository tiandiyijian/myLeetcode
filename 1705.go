package leetcode

import (
	"container/heap"
)

type Apple struct {
	day, cnt int
}

type AppleHeap []Apple

func (h AppleHeap) Less(i, j int) bool {
	return h[i].day < h[j].day
}

func (h AppleHeap) Len() int {
	return len(h)
}

func (h AppleHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *AppleHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func (h *AppleHeap) Push(x interface{}) {
	*h = append(*h, x.(Apple))
}

func (h *AppleHeap) Update(day int) {
	for i := 0; i < len(*h); i++ {
		(*h)[i].day -= day
	}
}

func (h *AppleHeap) Judge() int {
	for h.Len() > 0 && ((*h)[0].day == 0 || (*h)[0].cnt == 0) {
		heap.Pop(h)
	}
	if h.Len() > 0 {
		(*h)[0].cnt--
		return 1
	}
	return 0
}

func eatenApples(apples []int, days []int) int {
	// n := len(apples)
	h := &AppleHeap{}
	ans := 0
	for i, cnt := range apples {
		if cnt > 0 {
			heap.Push(h, Apple{days[i], cnt})
		}
		ans += h.Judge()
		h.Update(1)
	}
	// fmt.Println(h)
	for h.Len() > 0 {
		tmp := heap.Pop(h).(Apple)
		cnt := tmp.cnt
		day := tmp.day
		if day == 0 {
			continue
		}
		if cnt < day {
			ans += cnt
			h.Update(cnt)
		} else {
			ans += day
			h.Update(day)
		}
	}
	return ans
}

// func main() {
// 	apples := []int{1, 2, 3, 5, 2}
// 	days := []int{3, 2, 1, 4, 2}
// 	fmt.Println(eatenApples(apples, days))
// }
