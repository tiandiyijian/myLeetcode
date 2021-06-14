package leetcode

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	low, high := 1, n
	// var mid int
	for {
		mid := (low + high) >> 1
		if pick := guess(mid); pick == 0 {
			return mid
		} else if pick == 1 {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	// return mid
}
