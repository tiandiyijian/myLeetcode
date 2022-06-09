from bisect import bisect_left
import random
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # self.areas = list((y - b) * (x - a) for a, b, x, y in rects)
        # 因为只能取整数点, 所以不能用面积应该用点数
        self.points = list((y - b + 1) * (x - a + 1) for a, b, x, y in rects)
        for i in range(1, len(self.points)):
            self.points[i] += self.points[i - 1]

    def pick(self) -> List[int]:
        rnd = random.randint(1, self.points[-1])
        idx = bisect_left(self.points, rnd)
        a, b, x, y = self.rects[idx]
        return [random.randint(a, x), random.randint(b, y)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
