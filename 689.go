package leetcode

func maxSumOfThreeSubarrays(nums []int, k int) (ans []int) {
	n := len(nums)
	max1, idxMax1 := 0, -1
	max2, idxMax2_1, idxMax2_2 := 0, -1, -1
	max3, idxMax3 := 0, -1
	sum1, sum2, sum3 := 0, 0, 0
	//i1, i2 := -1, -1
	for i := 0; i < n-2*k; i++ {
		sum1 += nums[i]
		sum2 += nums[i+k]
		sum3 += nums[i+2*k]
		if i >= k-1 {
			if sum1 > max1 {
				max1 = sum1
				idxMax1 = i - k + 1
			}
			if tmp := sum2 + max1; tmp > max2 {
				max2 = tmp
				idxMax2_2 = i + 1
				idxMax2_1 = idxMax1
			}
			if tmp := max2 + sum3; tmp > max3 {
				max3 = tmp
				idxMax3 = i + k + 1
				//i2 = idxMax2_2
				//i1 = idxMax2_1
				ans = []int{idxMax2_1, idxMax2_2, idxMax3}
			}
			sum1 -= nums[i-k+1]
			sum2 -= nums[i+1]
			sum3 -= nums[i+k+1]
			//fmt.Println(i, idxMax1, max1, idxMax2, max2, idxMax3, max3)
		}
	}
	return
}
