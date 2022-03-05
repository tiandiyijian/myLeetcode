package leetcode

func numberOfGoodSubsets(nums []int) int {
	primes := [10]int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
	badNum := map[int]bool{}
	for _, v := range []int{4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28} {
		badNum[v] = true
	}
	mod := 1000000007

	cnter := map[int]int{}
	for _, v := range nums {
		cnter[v]++
	}

	f := [1 << 10]int{}
	f[0] = 1
	// outer:
	for num, cnt := range cnter {
		if num == 1 || badNum[num] {
			continue
		}
		mask := 0
		for i, p := range primes {
			// if num % (p*p) == 0 {
			//     continue outer
			// }
			if num%p == 0 {
				mask |= (1 << i)
				num /= p
			}
		}
		for pre_mask := 1023; pre_mask >= 0; pre_mask-- {
			if pre_mask&mask == 0 {
				f[pre_mask|mask] = (f[pre_mask|mask] + f[pre_mask]*cnt) % mod
			}
		}
	}
	ans := 0
	for _, v := range f[1:] {
		ans = (ans + v) % mod
	}
	for i := 0; i < cnter[1]; i++ {
		ans = (ans * 2) % mod
	}
	return ans
}
