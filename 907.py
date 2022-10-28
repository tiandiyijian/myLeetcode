from math import inf
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        s = [(-1, -inf)]
        for i, v in enumerate(arr):
            while v < s[-1][1]:
                idx, _ = s.pop()
                right[idx] = i
            left[i] = s[-1][0]
            s.append((i, v))

        while len(s) > 1:
            idx, _ = s.pop()
            right[idx] = n

        # print(left, right)
        return sum((right[i] - i) * (i - left[i]) * arr[i] for i in range(n)) % mod
