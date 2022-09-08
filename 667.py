from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 前半部分用一个递增序列
        # 后半部分凑一个刚好有k个不同的差的序列
        ans = [0] * n
        for i in range(n - k):
            ans[i] = i + 1

        a = n
        b = n - k + 1
        flagA = True
        for i in range(n - k, n):
            if flagA:
                ans[i] = a
                a -= 1
            else:
                ans[i] = b
                b += 1
            flagA = not flagA

        return ans
