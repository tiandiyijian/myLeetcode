from bisect import bisect_left, bisect_right
from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        piles.sort()
        lo = max(1, sum(piles) // h)
        hi = piles[-1]
        while lo < hi:
            # print(lo, hi)
            k = (lo + hi) >> 1
            idx = bisect_right(piles, k)
            if idx == n:
                t = len(piles)
            else:
                t = idx + sum(ceil(pile / k) for pile in piles[idx:])
            # print(k, idx, f'{t=}')
            if t > h:
                lo = k + 1
            else:
                hi = k
            # print()
        return lo


piles = [3, 6, 7, 11]
h = 8

piles = [312884470]
h = 968709470
print(Solution().minEatingSpeed(piles, h))
