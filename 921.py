class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # 不用使用栈保存括号，直接记录左括号数量即可
        ans = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    ans += 1

        return ans + cnt
