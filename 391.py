from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        total_area = 0
        left = bottom = float('inf')
        right = top = float('-inf')
        cnt = collections.defaultdict(int)

        for x, y, a, b in rectangles:
            total_area += (a - x) * (b - y)
            left = min(left, x)
            bottom = min(bottom, y)
            right = max(right, a)
            top = max(top, b)

            cnt[(x, y)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1
            cnt[(a, b)] += 1

        # print(total_area, left, right, bottom, top)
        if total_area != (right - left) * (top - bottom) or cnt[(left, bottom)] != 1 \
                or cnt[(left, top)] != 1 or cnt[(right, bottom)] != 1 or cnt[(right, top)] != 1:
            return False
        del cnt[(left, bottom)], cnt[(left, top)], cnt[(
            right, bottom)], cnt[(right, top)]
        return all(c == 2 or c == 4 for c in cnt.values())
