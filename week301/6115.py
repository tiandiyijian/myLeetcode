from functools import cache
from math import comb


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        # 看答案也看不懂
        MOD = 10 ** 9 + 7
        ans = 0

        @cache
        def f(cnt):
            return comb(n-1, cnt-1)

        pass


n = 2
maxValue = 5
n = 5
maxValue = 9
print(Solution().idealArrays(n, maxValue))