package leetcode

func slowestKey(releaseTimes []int, keysPressed string) byte {
	ans := keysPressed[0]
	time := releaseTimes[0]
	for i := 1; i < len(releaseTimes); i++ {
		if tmp := releaseTimes[i] - releaseTimes[i-1]; tmp > time {
			time = tmp
			ans = keysPressed[i]
		} else if tmp == time {
			if keysPressed[i] > ans {
				ans = keysPressed[i]
			}
		}
	}
	return ans
}
