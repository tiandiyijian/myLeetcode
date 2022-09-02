from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        n = len(arr)

        def closer(l, r):
            if l < 0:
                return r
            if r >= n:
                return l
            if x - arr[l] > arr[r] - x:
                return r
            return l

        l = idx - 1
        r = idx
        # right = []
        # left = []
        for _ in range(k):
            if r == closer(l, r):
                # right.append(arr[r])
                r += 1
            else:
                # left.append(arr[l])
                l -= 1

        return arr[l+1:r]
