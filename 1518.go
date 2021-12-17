package leetcode

func numWaterBottles(numBottles int, numExchange int) int {
	cnt := numBottles / (numExchange - 1)
	if numBottles%(numExchange-1) == 0 {
		return numBottles + cnt - 1
	}
	return numBottles + cnt
}
