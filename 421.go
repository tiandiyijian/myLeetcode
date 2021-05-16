package leetcode

func findMaximumXOR(nums []int) int {
	HIGH_BIT := 30
	x := 0
	for k := HIGH_BIT; k >= 0; k-- {
		seen := make(map[int]bool)
		for _, num := range nums {
			seen[num>>k] = true
		}
		x_next := x<<1 + 1
		found := false
		for _, num := range nums {
			if _, ok := seen[x_next^(num>>k)]; ok {
				found = true
				break
			}
		}
		if found {
			x = x_next
		} else {
			x = x_next - 1
		}
	}
	return x
}
