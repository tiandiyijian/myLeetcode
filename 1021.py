class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        n = len(s)
        i = 0
        cnt = 1
        while i < n:
            j = i + 1
            while j < n and cnt > 0:
                if s[j] == ')':
                    cnt -= 1
                else:
                    cnt += 1
                j += 1
            ans += s[i + 1 : j - 1]
            i = j
            cnt = 1
        return ans
