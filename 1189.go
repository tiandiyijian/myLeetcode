package leetcode

func maxNumberOfBalloons(text string) int {
	var b, a, l, o, n int
	for i := 0; i < len(text); i++ {
		if text[i] == 'b' {
			b++
		} else if text[i] == 'a' {
			a++
		} else if text[i] == 'l' {
			l++
		} else if text[i] == 'o' {
			o++
		} else if text[i] == 'n' {
			n++
		}
	}
	l >>= 1
	o >>= 1
	ans := b
	if ans > a {
		ans = a
	}
	if ans > l {
		ans = l
	}
	if ans > o {
		ans = o
	}
	if ans > n {
		ans = n
	}
	return ans
}
