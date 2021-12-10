package leetcode

import (
	"unicode"
)

func shortestCompletingWord(licensePlate string, words []string) string {
	cnt := map[rune]int{}
	for _, r := range licensePlate {
		if unicode.IsLetter(r) {
			cnt[unicode.ToLower(r)]++
		}
	}
	var ans string
	ans_len := 1000
outer:
	for _, w := range words {
		if len(w) < ans_len {
			cntW := map[rune]int{}
			for _, r := range w {
				cntW[r]++
			}
			for key, val := range cnt {
				if val > cntW[key] {
					continue outer
				}
			}
			ans = w
			ans_len = len(ans)
		}
	}
	return ans
}

// func main() {
// 	a := "1s3 PSt"
// 	b := []string{"step", "steps"}
// 	fmt.Println(shortestCompletingWord(a, b))
// }
