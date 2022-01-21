package leetcode

func minJumps(arr []int) int {
	n := len(arr)
	if n == 1 {
		return 0
	}
	value_idx := map[int][]int{}
	for i, num := range arr {
		value_idx[num] = append(value_idx[num], i)
	}
	q := []int{0}
	visit := map[int]bool{}
	visit[0] = true
	path := 1
	for {
		new_q := []int{}
		for _, i := range q {
			same_value_indices := value_idx[arr[i]]
			if len(same_value_indices) > 1 {
				for _, idx := range same_value_indices {
					if _, ok := visit[idx]; idx != i && !ok {
						if idx == n-1 {
							return path
						}
						new_q = append(new_q, idx)
						visit[idx] = true
					}
				}
			}
			// 对于相同value即相邻的节点，第一次访问后既可把这个value从map中删除，这样访问后续的节点时就不用再遍历一次了(即使这些相邻节点都已经在visit里面了，但遍历一次还是很耗时)
			delete(value_idx, arr[i])
			if !visit[i-1] && i-1 >= 0 {
				if i-1 == n-1 {
					return path
				}
				visit[i-1] = true
				new_q = append(new_q, i-1)
			}
			if !visit[i+1] && i+1 < n {
				if i+1 == n-1 {
					return path
				}
				visit[i+1] = true
				new_q = append(new_q, i+1)
			}
		}
		q = new_q
		path++
	}
}
