package leetcode

func removeInvalidParentheses(s string) []string {
	isValid := func(s string) bool {
		cnt := 0
		for _, c := range s {
			if c == '(' {
				cnt += 1
			} else if c == ')' {
				cnt -= 1
				if cnt < 0 {
					return false
				}
			}
		}
		return cnt == 0
	}

	curSet := map[string]struct{}{s: {}}
	ans := []string{}
	for len(curSet) > 0 {
		nextSet := map[string]struct{}{}
		for str := range curSet {
			if isValid(str) {
				ans = append(ans, str)
			}
			if len(ans) == 0 {
				for i := range str {
					if i > 0 && str[i] == str[i-1] {
						continue
					}
					nextSet[str[:i]+str[i+1:]] = struct{}{}
				}
			}
		}
		if len(ans) > 0 {
			return ans
		}
		curSet = nextSet
	}
	return ans
}
