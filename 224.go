package leetcode

import (
	"strconv"
	"unicode"
)

func calculate(s string) int {
	operand := []int{}
	operator := []byte{}
	// ans := 0
	i := 0
	n := len(s)
	flag := false
	for i < n {
		if unicode.IsDigit(rune(s[i])) {
			j := i + 1
			for j < n && unicode.IsDigit(rune(s[j])) {
				j++
			}
			op, _ := strconv.Atoi(s[i:j])
			if flag {
				op = -op
				flag = false
				operator = operator[:len(operator)-1]
			}
			operand = append(operand, op)
			i = j
		} else {
			switch s[i] {
			case '(':
				operator = append(operator, '(')
				flag = false
			case ')':
				for operator[len(operator)-1] != '(' {
					op2, op1 := operand[len(operand)-1], operand[len(operand)-2]
					switch operator[len(operator)-1] {
					case '+':
						operand[len(operand)-2] = op1 + op2
					case '-':
						operand[len(operand)-2] = op1 - op2
					}
					operand = operand[:len(operand)-1]
					operator = operator[:len(operator)-1]
				}
				operator = operator[:len(operator)-1]
				if len(operator) > 0 {
					if operator[len(operator)-1] == '^' {
						operator = operator[:len(operator)-1]
						operand[len(operand)-1] = -operand[len(operand)-1]
					}
				}
			case '-', '+':
				if s[i] == '-' && (i == 0 || s[i-1] == '(') {
					operator = append(operator, '^')
					flag = true
					break
				}
				if len(operator) > 0 && len(operand) > 1 && operator[len(operator)-1] != '(' {
					op2, op1 := operand[len(operand)-1], operand[len(operand)-2]
					switch operator[len(operator)-1] {
					case '+':
						operand[len(operand)-2] = op1 + op2
					case '-':
						operand[len(operand)-2] = op1 - op2
					}
					operand = operand[:len(operand)-1]
					operator = operator[:len(operator)-1]
				}
				operator = append(operator, s[i])
			}
			i++
		}
		// fmt.Println(operand, operator)
	}
	// fmt.Println(operand, operator)
	for len(operator) > 0 {
		if operator[len(operator)-1] == '^' {
			operator = operator[:len(operator)-1]
			operand[len(operand)-1] = -operand[len(operand)-1]
			continue
		}
		op2, op1 := operand[len(operand)-1], operand[len(operand)-2]
		switch operator[len(operator)-1] {
		case '+':
			operand[len(operand)-2] = op1 + op2
		case '-':
			operand[len(operand)-2] = op1 - op2
		}
		operand = operand[:len(operand)-1]
		operator = operator[:len(operator)-1]
	}
	// if len(operator) > 0 && len(operand) == 1 {
	// 	return -operand[0]
	// }
	return operand[0]
}

// 因为只有加法和减法，其实可以不用这么一板一眼地做，对于每一个数字都可以判断它的符号（不管在不在括号里）
func calculate2(s string) int {
	ans := 0
	operator := []int{1}
	num := 0
	sign := 1
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			continue
		}
		if unicode.IsDigit(rune(s[i])) {
			num = num*10 + int(s[i]-'0')
		} else {
			ans += sign * num
			num = 0
			if s[i] == '+' {
				sign = operator[len(operator)-1]
			} else if s[i] == '-' {
				sign = -operator[len(operator)-1]
			} else if s[i] == '(' {
				operator = append(operator, sign)
			} else {
				operator = operator[:len(operator)-1]
			}
		}
	}
	return ans
}
