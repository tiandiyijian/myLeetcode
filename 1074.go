package leetcode

func subarraySum(nums []int, k int) (ans int) {
	mp := map[int]int{0: 1}
	sum := 0
	for _, val := range nums {
		sum += val
		if val, ok := mp[sum-k]; ok {
			ans += val
		}
		mp[sum]++
	}
	return
}

func numSubmatrixSumTarget(matrix [][]int, target int) int {
	ans := 0
	n := len(matrix[0])
	for i := range matrix {
		sum := make([]int, n)
		for _, row := range matrix[i:] {
			for k, val := range row {
				sum[k] += val
			}
			ans += subarraySum(sum, target)
		}
	}
	return ans
}
