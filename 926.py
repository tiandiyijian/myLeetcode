class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # 遍历每一个分界点
        # 把分界点前面的1和后面的0翻转
        cnt = s.count('0')
        ans = cnt
        for c in s:
            if c == '1':
                cnt += 1
            else:
                cnt -= 1
            ans = min(ans, cnt)
        return ans
