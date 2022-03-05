package leetcode

func sumOfUnique(nums []int) int {
	cnter := map[int]int{}
	for _, num := range nums {
		cnter[num]++
	}
	ans := 0
	for num, cnt := range cnter {
		if cnt == 1 {
			ans += num
		}
	}
	return ans
}
