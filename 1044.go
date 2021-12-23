package leetcode

import (
	"math"
	"math/rand"
)

func randInt(a, b int) int {
	return a + rand.Intn(b-a)
}

func pow(x, n, mod int) (ans int) {
	ans = 1
	for ; n > 0; n >>= 1 {
		if n&1 == 1 {
			ans = ans * x % mod
		}
		x = x * x % mod
		// fmt.Println("pow", ans, x)
	}
	return
}

func longestDupSubstring(s string) string {
	a1, a2 := randInt(26, 100), randInt(26, 100)
	mod1, mod2 := randInt(1e9+7, math.MaxInt32), randInt(1e9+7, math.MaxInt32)
	n := len(s)
	s_int := make([]int, n)
	for i, r := range s {
		s_int[i] = int(r) - 'a'
	}

	check := func(m int) int {
		aL1, aL2 := pow(a1, m, mod1), pow(a2, m, mod2)
		// fmt.Println(m)
		// fmt.Println(a1, aL1, a2, aL2)
		hash1, hash2 := 0, 0
		for i := 0; i < m; i++ {
			hash1 = (hash1*a1 + s_int[i]) % mod1
			hash2 = (hash2*a2 + s_int[i]) % mod2
		}
		// fmt.Println(hash1, hash2)
		seen := map[[2]int]struct{}{{hash1, hash2}: {}}
		for start := 1; start < n-m+1; start++ {
			// fmt.Println(start)
			hash1 = (hash1*a1 - s_int[start-1]*aL1 + s_int[start+m-1]) % mod1
			if hash1 < 0 {
				hash1 += mod1
			}
			hash2 = (hash2*a2 - s_int[start-1]*aL2 + s_int[start+m-1]) % mod2
			if hash2 < 0 {
				hash2 += mod2
			}
			// if start == 2 {
			// 	fmt.Println(hash1, hash2, seen)
			// }
			tmp := [2]int{hash1, hash2}
			if _, ok := seen[tmp]; ok {
				return start
			}
			seen[tmp] = struct{}{}
		}
		return -1
	}

	low, high := 1, n-1
	start, length := -1, 0
	for low <= high {
		mid := low + (high-low+1)/2
		// fmt.Println(low, high, mid)
		idx := check(mid)
		if idx != -1 {
			start = idx
			length = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	// fmt.Println(check(3))
	// fmt.Println("---", pow(53, 3, mod1))
	if start != -1 {
		return s[start : start+length]
	}
	return ""
}

// func main() {
// 	fmt.Println(longestDupSubstring("anana"))
// }
