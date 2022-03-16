package leetcode

import "container/heap"

type item struct {
	key              string
	cnt              int
	idx_min, idx_max int
}

type minHeap []*item

func (h minHeap) Len() int { return len(h) }

func (h minHeap) Less(i, j int) bool { return h[i].cnt < h[j].cnt }

func (h minHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].idx_min = i
	h[j].idx_min = j
}

func (h *minHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	x.idx_min = -1
	(*h)[n-1] = nil
	*h = (*h)[:n-1]
	return x
}

func (h *minHeap) Push(x interface{}) {
	n := len(*h)
	X := x.(*item)
	X.idx_min = n
	(*h) = append((*h), X)
}

type maxHeap []*item

func (h maxHeap) Len() int { return len(h) }

func (h maxHeap) Less(i, j int) bool { return h[i].cnt > h[j].cnt }

func (h maxHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].idx_max = i
	h[j].idx_max = j
}

func (h *maxHeap) Pop() interface{} {
	n := len(*h)
	x := (*h)[n-1]
	x.idx_max = -1
	(*h)[n-1] = nil
	*h = (*h)[:n-1]
	return x
}

func (h *maxHeap) Push(x interface{}) {
	n := len(*h)
	X := x.(*item)
	X.idx_max = n
	(*h) = append((*h), X)
}

type AllOne struct {
	minHeap *minHeap
	maxHeap *maxHeap
	mp      map[string]*item
}

func Constructor() AllOne {
	return AllOne{
		minHeap: new(minHeap),
		maxHeap: new(maxHeap),
		mp:      make(map[string]*item),
	}
}

func (this *AllOne) Inc(key string) {
	if x, ok := this.mp[key]; ok {
		x.cnt++
		heap.Fix(this.minHeap, x.idx_min)
		heap.Fix(this.maxHeap, x.idx_max)
	} else {
		x = new(item)
		x.key = key
		x.cnt = 1
		heap.Push(this.minHeap, x)
		heap.Push(this.maxHeap, x)
		this.mp[key] = x
	}
}

func (this *AllOne) Dec(key string) {
	x := this.mp[key]
	if x.cnt == 1 {
		delete(this.mp, key)
		heap.Remove(this.minHeap, x.idx_min)
		heap.Remove(this.maxHeap, x.idx_max)
	} else {
		x.cnt--
		heap.Fix(this.minHeap, x.idx_min)
		heap.Fix(this.maxHeap, x.idx_max)
	}
}

func (this *AllOne) GetMaxKey() string {
	if len(this.mp) == 0 {
		return ""
	}
	return (*this.maxHeap)[0].key
}

func (this *AllOne) GetMinKey() string {
	if len(this.mp) == 0 {
		return ""
	}
	// print(*this.minHeap)
	// print(*this.maxHeap)
	return (*this.minHeap)[0].key
}

// func print(h []*item) {
// 	for _, v := range h {
// 		fmt.Printf("%v ", v)
// 	}
//     fmt.Println()
// }

/**
 * Your AllOne object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Inc(key);
 * obj.Dec(key);
 * param_3 := obj.GetMaxKey();
 * param_4 := obj.GetMinKey();
 */
