package leetcode

func maxSlidingWindow(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	q := []int{}
	for i := 0; i < k; i++ {
		for len(q) > 0 && nums[q[len(q)-1]] <= nums[i] {
			q = q[:len(q)-1]
		}
		q = append(q, i)
	}
	ans[0] = nums[q[0]]
	cur := 1
	// fmt.Println(0, q)
	for i := k; i < n; i++ {
		for len(q) > 0 && nums[q[len(q)-1]] <= nums[i] {
			q = q[:len(q)-1]
		}
		q = append(q, i)
		// fmt.Println(cur, q)
		if q[0] < cur {
			q = q[1:]
		}
		ans[cur] = nums[q[0]]
		cur++
	}
	return ans
}

func maxSlidingWindow2(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	q := []int{}
	for i := 0; i < k; i++ {
		for len(q) > 0 && q[len(q)-1] < nums[i] {
			q = q[:len(q)-1]
		}
		q = append(q, nums[i])
	}
	ans[0] = q[0]
	cur := 1
	for i := k; i < n; i++ {
		for len(q) > 0 && q[len(q)-1] < nums[i] {
			q = q[:len(q)-1]
		}
		q = append(q, nums[i])

		// 如果把上面改成q[len(q)-1] <= nums[i]的话就不可以这么判断
		// 比如说这个样例[-7,-8,7,5,7,1,6,0], 4, 此时会存在nums[6-4] == q[0]的情况
		// 但是如果队头出队的话出的实际上是第4个元素即第2个7
		// 我还是更喜欢上面的写法，绝对不会出错，入队的是元素下标而不是元素值
		// fmt.Println(i, q)
		if q[0] == nums[i-k] {
			q = q[1:]
		}
		ans[cur] = q[0]
		cur++
	}
	return ans
}
