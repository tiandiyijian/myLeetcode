package leetcode

func isAdditiveNumber(num string) bool {
	n := len(num)
	if n < 3 {
		return false
	}
	zero := byte('0')
	nine := byte('9')

	var add func(s1, l1, s2, l2 int) string
	add = func(s1, l1, s2, l2 int) string {
		if l1 < l2 {
			return add(s2, l2, s1, l1)
		}
		ans := make([]byte, l1)
		carry := byte(0)
		for i1, i2 := l1-1, l2-1; i1 >= 0; i1-- {
			n2 := zero
			if i2 >= 0 {
				n2 = num[s2+i2]
			}
			tmp := num[s1+i1] + n2 - zero + carry
			if tmp > nine {
				carry = 1
				tmp -= 10
			} else {
				carry = 0
			}
			// fmt.Println(i1, num[s1+i1], n2)
			ans[i1] = tmp
			i2--
		}
		if carry > 0 {
			return "1" + string(ans)
		}
		return string(ans)
	}

	var validate func(s1, l1, s2, l2 int) bool
	validate = func(s1, l1, s2, l2 int) bool {
		third := add(s1, l1, s2, l2)
		s3 := s2 + l2
		l3 := len(third)
		for i := 0; i < l3; i++ {
			if s3+i >= n {
				return false
			}
			if third[i] != num[s3+i] {
				return false
			}
		}
		if s3+l3 == n {
			return true
		}
		return validate(s2, l2, s3, l3)
	}

	for i := 0; i <= n/3; i++ {
		s1 := 0
		l1 := i + 1
		s2 := i + 1
		if num[s2] == zero {
			if validate(s1, l1, s2, 1) {
				return true
			}
			continue
		}
		for j := i + 1; j <= 2*n/3 && j < n; j++ {
			l2 := j - i
			if validate(s1, l1, s2, l2) {
				return true
			}
		}
	}
	return false
}

// func main() {
// 	s := "198019823962"
// 	fmt.Println(isAdditiveNumber(s))
// }
