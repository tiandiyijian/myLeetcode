from itertools import pairwise
from typing import List


MOD = int(1e9 + 7)
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        xs, ans = set(), 0
        for x0, _, x1, _ in rectangles:
            xs.add(x0)
            xs.add(x1)
        # 纵向x轴扫描线
        for a, b in pairwise(sorted(xs)):
            ys = [(y0, y1) for x0, y0, x1, y1 in rectangles if x0 <= a and b <= x1]
            s = cur = 0
            # 横向y轴扫描线
            for c, d in sorted(ys, key=lambda x: (x[0], -x[1])):
                if c > cur:
                    s += d - c
                elif d > cur:
                    s += d - cur
                cur = max(cur, d)
            ans = (ans + s * (b - a)) % MOD
        return ans
