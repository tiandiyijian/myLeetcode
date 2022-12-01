from math import inf
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        d = inf
        ans = -1
        for i, (a, b) in enumerate(points):
            if (a == x or b == y) and (tmp := abs(a - x) + abs(b - y)) < d:
                d = tmp
                ans = i
        return ans
