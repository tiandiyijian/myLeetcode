package leetcode

func isOneBitCharacter(bits []int) bool {
	i := 0
	n := len(bits)
	for i < n-1 {
		if bits[i] == 1 {
			i += 2
		} else {
			i += 1
		}
	}
	return i == n-1
}
