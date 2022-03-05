package leetcode

func pushDominoes(dominoes string) string {
	n := len(dominoes)
	i := 0
	var L, R byte = 'L', 'R'
	ans := []byte(dominoes)
	for i < n {
		if ans[i] == '.' {
			j := i
			for ; j < n && ans[j] == '.'; j++ {
			}

			l := L
			if i > 0 {
				l = ans[i-1]
			}

			r := R
			if j < n {
				r = ans[j]
			}

			if l == r {
				for k := i; k < j; k++ {
					ans[k] = l
				}
			} else {
				if l == R && r == L {
					for p, q := i, j-1; p < q; p++ {
						ans[p] = R
						ans[q] = L
						q--
					}
				}
			}
			i = j
		} else {
			i++
		}
	}
	return string(ans)
}
