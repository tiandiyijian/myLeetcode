package leetcode

func candy(ratings []int) int {
	n := len(ratings)
	inc, dec := 1, 0
	total := 1
	for i := 1; i < n; i++ {
		if ratings[i] >= ratings[i-1] {
			if ratings[i] > ratings[i-1] {
				if dec > 0 { // 此时是递增数组的第二个元素
					inc = 1
				}
				inc++
			} else {
				inc = 1
			}
			total += inc
			dec = 0
		} else {
			dec++
			if dec == inc {
				// 这是最妙的一步，如果当前的递减数组的长度等于前面那一个递增数组的长度
				// 那么这一步相当于把前面的哪个递增数组的最后一个元素并入现在这个递减数组中
				dec++
			}
			total += dec
		}
	}
	return total
}
