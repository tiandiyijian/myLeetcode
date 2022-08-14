from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zero_cnt = sum(c == '0' for c in s)
        one_cnt = n - zero_cnt

        ans = 0
        cur_zero = 0
        cur_one = one_cnt
        for i in range(n-1):
            if s[i] == '0':
                cur_zero += 1
            else:
                cur_one -= 1
            ans = max(cur_zero + cur_one, ans)
        
        return ans
                