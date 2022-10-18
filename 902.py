from functools import cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        num = [c for c in str(n)]
        n = len(num)
        m = len(digits)

        # 位数比n小的
        ans = 0
        cur = 1
        for _ in range(1, n):
            cur *= m
            ans += cur

        # 位数和n一样的
        @cache
        def dfs(pos, bound):
            # bound表示该位前面是否贴着上界
            if pos == n:
                return 1

            ret = 0
            for c in digits:
                if bound:
                    if ord(c) > ord(num[pos]):
                        break
                    elif ord(c) == ord(num[pos]):
                        ret += dfs(pos + 1, True)
                    else:
                        ret += dfs(pos + 1, False)
                else:
                    ret += dfs(pos + 1, False)
            return ret

        return ans + dfs(0, True)
