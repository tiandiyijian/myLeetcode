package leetcode

func maxPower(s string) int {
	// ans := 0
	// l := 0
	// for r := 1; r < len(s); r++ {
	//     if s[r] != s[l]{
	//         if tmp := r - l; tmp > ans {
	//             ans = tmp
	//         }
	//         l = r
	//     }
	// }
	// if tmp := len(s) - l; tmp > ans {
	//     ans = tmp
	// }
	// return ans
	var (
		ans = 0
		cnt = 1
	)
	for i := 1; i < len(s); i++ {
		if s[i] != s[i-1] {
			if cnt > ans {
				ans = cnt
			}
			cnt = 1
		} else {
			cnt++
		}
	}
	if cnt > ans {
		ans = cnt
	}
	return ans
}
