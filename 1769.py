from itertools import accumulate
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        indices = [i for i, b in enumerate(boxes) if b == '1']
        m = len(indices)
        pre_sum = list(accumulate(indices))
        ans = [0] * n
        if m == 0:
            return ans

        p = 0
        for i in range(n):
            while p < m and indices[p] < i:
                p += 1
            ans[i] += pre_sum[-1] - (pre_sum[p - 1] if p > 0 else 0) - i * (m - p)
            ans[i] += i * p - (pre_sum[p - 1] if p > 0 else 0)
        return ans
