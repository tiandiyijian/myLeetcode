package leetcode

type DetectSquares struct {
	points [1001]map[int]int
}

func Constructor() DetectSquares {
	points := [1001]map[int]int{}
	for i := 0; i < 1001; i++ {
		points[i] = map[int]int{}
	}
	return DetectSquares{points}
}

func (this *DetectSquares) Add(point []int) {
	this.points[point[0]][point[1]]++
}

func (this *DetectSquares) Count(point []int) int {
	ys := this.points[point[0]]
	x0, y0 := point[0], point[1]
	ans := 0
	for y, cnt := range ys {
		if y == y0 {
			continue
		}
		length := y - y0
		if length < 0 {
			length = -length
		}
		// (x1, y), (x1, y0)
		x1 := x0 - length
		if 0 <= x1 && x1 <= 1000 {
			cnt1 := this.points[x1][y]
			cnt2 := this.points[x1][y0]
			ans += cnt * cnt1 * cnt2
		}
		x1 = x0 + length
		if 0 <= x1 && x1 <= 1000 {
			cnt1 := this.points[x1][y]
			cnt2 := this.points[x1][y0]
			ans += cnt * cnt1 * cnt2
		}
	}
	return ans
}

/**
 * Your DetectSquares object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(point);
 * param_2 := obj.Count(point);
 */
