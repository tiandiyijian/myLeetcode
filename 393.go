package leetcode

func validUtf8(data []int) bool {
	n := len(data)
	for i := 0; i < n; {
		if l := utf8Len(data[i]); l == 1 {
			i++
		} else if l == 2 {
			if i+1 < n && startWith10(data[i+1]) {
				i += 2
			} else {
				return false
			}
		} else if l == 3 {
			for j := i + 1; j <= i+2; j++ {
				if j >= n || !startWith10(data[j]) {
					return false
				}
			}
			i += 3
		} else if l == 4 {
			for j := i + 1; j <= i+3; j++ {
				if j >= n || !startWith10(data[j]) {
					return false
				}
			}
			i += 4
		} else {
			return false
		}
	}
	return true
}

func utf8Len(data int) int {
	if data&0b11111000 == 0b11110000 {
		return 4
	}
	if data&0b11110000 == 0b11100000 {
		return 3
	}
	if data&0b11100000 == 0b11000000 {
		return 2
	}
	if data&0b10000000 == 0 {
		return 1
	}
	return 0
}

func startWith10(data int) bool {
	return data&0b10000000 == 0b10000000
}
