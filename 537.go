package leetcode

import (
	"fmt"
	"strconv"
	"strings"
)

func complexNumberMultiply(num1 string, num2 string) string {
	a1, b1 := parseString(num1)
	a2, b2 := parseString(num2)
	real := a1*a2 - b1*b2
	imag := a1*b2 + a2*b1
	// fmt.Println(a1, b1, a2, b2)
	// fmt.Println(real, imag)
	return fmt.Sprintf("%d+%di", real, imag)
}

func parseString(s string) (a, b int) {
	sign := 1
	i := 0
	if s[0] == '+' {
		sign = 1
		i = 1
	} else if s[0] == '-' {
		sign = -1
		i = 1
	}

	for '0' <= s[i] && s[i] <= '9' {
		a = a*10 + int(s[i]-'0')
		i++
	}
	a *= sign
	i++

	sign = 1
	if s[i] == '-' {
		sign = -1
		i++
	}
	for i < len(s) && '0' <= s[i] && s[i] <= '9' {
		b = b*10 + int(s[i]-'0')
		i++
	}
	b *= sign
	return a, b
}

func parseComplexNumber(num string) (real, imag int) {
	// 其实只会在中间出现一个加号作为运算符
	i := strings.IndexByte(num, '+')
	real, _ = strconv.Atoi(num[:i])
	imag, _ = strconv.Atoi(num[i+1 : len(num)-1])
	return
}
