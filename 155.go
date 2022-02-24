package leetcode

type MinStack struct {
	s    []int
	minS []int
	n    int
	// min int
}

func Constructor() MinStack {
	return MinStack{}
}

func (this *MinStack) Push(val int) {
	var min int
	if this.n == 0 {
		min = val
	} else {
		min = this.minS[this.n-1]
		if min > val {
			min = val
		}
	}
	if this.n == len(this.s) {
		this.s = append(this.s, val)
		this.minS = append(this.minS, min)
	} else {
		this.s[this.n] = val
		this.minS[this.n] = min
	}
	this.n++
}

func (this *MinStack) Pop() {
	this.n--
}

func (this *MinStack) Top() int {
	return this.s[this.n-1]
}

func (this *MinStack) GetMin() int {
	return this.minS[this.n-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
