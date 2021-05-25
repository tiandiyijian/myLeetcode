package leetcode

func generateParenthesis(n int) []string {
	ans := []string{}
	helper("", n, n, &ans)
	return ans
}

func helper(s string, left, right int, ans *[]string) {
	if left == 0 && right == 0 {
		*ans = append(*ans, s)
		return
	}
	if left > 0 {
		helper(s+"(", left-1, right, ans)
	}
	if left < right {
		helper(s+")", left, right-1, ans)
	}
}
