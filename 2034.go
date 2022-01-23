package leetcode

import "container/heap"

type stock struct {
	time, price, indexMin, indexMax int
}

type MinStockHeap []*stock

func (h MinStockHeap) Len() int { return len(h) }

func (h MinStockHeap) Less(i, j int) bool {
	return h[i].price < h[j].price
}

func (h MinStockHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].indexMin = i
	h[j].indexMin = j
}

func (h *MinStockHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	old[n-1] = nil
	*h = old[:n-1]
	return x
}

func (h *MinStockHeap) Push(x interface{}) {
	n := len(*h)
	X := x.(*stock)
	X.indexMin = n
	*h = append(*h, X)
}

type MaxStockHeap []*stock

func (h MaxStockHeap) Len() int { return len(h) }

func (h MaxStockHeap) Less(i, j int) bool {
	return h[i].price > h[j].price
}

func (h MaxStockHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
	h[i].indexMax = i
	h[j].indexMax = j
}

func (h *MaxStockHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	old[n-1] = nil
	*h = old[:n-1]
	return x
}

func (h *MaxStockHeap) Push(x interface{}) {
	n := len(*h)
	X := x.(*stock)
	X.indexMax = n
	*h = append(*h, X)
}

type StockPrice struct {
	data         map[int]*stock
	maxHeap      *MaxStockHeap
	minHeap      *MinStockHeap
	currentStock *stock
}

func Constructor() StockPrice {
	return StockPrice{
		data:    map[int]*stock{},
		maxHeap: &MaxStockHeap{},
		minHeap: &MinStockHeap{},
	}
}

func (this *StockPrice) Update(timestamp int, price int) {
	if _, ok := this.data[timestamp]; ok {
		s := this.data[timestamp]
		s.price = price
		heap.Fix(this.maxHeap, s.indexMax)
		heap.Fix(this.minHeap, s.indexMin)
	} else {
		s := &stock{
			time:  timestamp,
			price: price,
		}
		this.data[timestamp] = s
		heap.Push(this.maxHeap, s)
		heap.Push(this.minHeap, s)
		if this.currentStock == nil || this.currentStock.time < timestamp {
			this.currentStock = s
		}
	}
}

func (this *StockPrice) Current() int {
	return this.currentStock.price
}

func (this *StockPrice) Maximum() int {
	return (*this.maxHeap)[0].price
}

func (this *StockPrice) Minimum() int {
	return (*this.minHeap)[0].price
}

/**
 * Your StockPrice object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Update(timestamp,price);
 * param_2 := obj.Current();
 * param_3 := obj.Maximum();
 * param_4 := obj.Minimum();
 */
