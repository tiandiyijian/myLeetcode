package leetcode

/*
 * @lc app=leetcode.cn id=1190 lang=golang
 *
 * [1190] 反转每对括号间的子串
 */

// @lc code=start
func reverseParentheses(s string) string {
	n := len(s)
	pair := make([]int, n)
	stk := []int{}
	for i, c := range s {
		if sc := string(c); sc == "(" {
			stk = append(stk, i)
		} else if sc == ")" {
			j := stk[len(stk)-1]
			pair[i] = j
			pair[j] = i
			stk = stk[:len(stk)-1]
		}
	}
	ans := []byte{}
	step := 1
	for ix := 0; ix < n; ix += step {
		if s[ix] == '(' || s[ix] == ')' {
			ix = pair[ix]
			step = -step
		} else {
			ans = append(ans, s[ix])
		}
	}
	return string(ans)
}

// @lc code=end
