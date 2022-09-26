from functools import cache


class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        digits = [int(digit) for digit in str(n)]

        @cache
        def dfs(pos: int, bound: bool, diff: bool) -> int:
            # pos 是从左向右第几位
            # bound 是当前位是否受到原值这一位最大值的约束
            # 因为不能比原值大，也可以描述为当前位之前的位是否和原值一样
            # diff 是是否包含2/5/6/9中至少一个
            
            if pos == len(digits):
                return int(diff)

            ret = 0
            for i in range(0, (digits[pos] if bound else 9) + 1):
                if valid[i] != -1:
                    ret += dfs(
                        pos + 1, bound and i == digits[pos], diff or valid[i] == 1
                    )

            return ret

        ans = dfs(0, True, False)
        return ans
