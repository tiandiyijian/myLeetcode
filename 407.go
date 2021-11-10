package leetcode

import "container/heap"

type Point struct {
	row, col, waterHeight int
}

type Points []Point

func (ps Points) Len() int {
	return len(ps)
}

func (ps Points) Less(i, j int) bool {
	return ps[i].waterHeight < ps[j].waterHeight
}

func (ps Points) Swap(i, j int) {
	ps[i], ps[j] = ps[j], ps[i]
}

func (ps *Points) Push(x interface{}) {
	*ps = append(*ps, x.(Point))
}

func (ps *Points) Pop() (x interface{}) {
	n := len(*ps)
	x = (*ps)[n-1]
	*ps = (*ps)[:n-1]
	return x
}

func trapRainWater(heightMap [][]int) int {
	m, n := len(heightMap), len(heightMap[0])
	pointHeap := &Points{}
	visited := make([][]bool, m)
	for i := range heightMap {
		visited[i] = make([]bool, n)
		for j := range heightMap[i] {
			if i == 0 || j == 0 || i == m-1 || j == n-1 {
				heap.Push(pointHeap, Point{i, j, heightMap[i][j]})
				visited[i][j] = true
			}
		}
	}

	ans := 0
	dirs := []int{-1, 0, 1, 0, -1}
	for len(*pointHeap) > 0 {
		minHeightPoint := heap.Pop(pointHeap).(Point)
		x, y, minHeight := minHeightPoint.row, minHeightPoint.col, minHeightPoint.waterHeight
		for k := 0; k < 4; k++ {
			dx, dy := dirs[k], dirs[k+1]
			nx, ny := x+dx, y+dy
			if 0 <= nx && nx < m && 0 <= ny && ny < n && !visited[nx][ny] {
				if heightMap[nx][ny] < minHeight {
					ans += minHeight - heightMap[nx][ny]
					heap.Push(pointHeap, Point{nx, ny, minHeight})
				} else {
					heap.Push(pointHeap, Point{nx, ny, heightMap[nx][ny]})
				}
				visited[nx][ny] = true
			}
		}
	}
	return ans
}
