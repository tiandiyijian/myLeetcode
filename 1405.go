package leetcode

import "sort"

type Pair struct {
	char byte
	cnt  int
}

type ByCnt []Pair

func (bc ByCnt) Len() int { return len(bc) }

func (bc ByCnt) Swap(i, j int) {
	bc[i], bc[j] = bc[j], bc[i]
}
func (bc ByCnt) Less(i, j int) bool {
	return bc[i].cnt > bc[j].cnt
}

func longestDiverseString(a int, b int, c int) string {
	ans := []byte{}
	bc := ByCnt{
		{'a', a},
		{'b', b},
		{'c', c},
	}
	total := a + b + c
	sort.Sort(bc)
	for total > 0 {
		if size := len(ans); size >= 2 && ans[size-1] == bc[0].char && ans[size-2] == bc[0].char {
			if bc[1].cnt > 0 {
				ans = append(ans, bc[1].char)
				bc[1].cnt--
			} else {
				return string(ans)
			}
		} else {
			ans = append(ans, bc[0].char)
			bc[0].cnt--
		}
		sort.Sort(bc)
		total--
	}
	return string(ans)
}
