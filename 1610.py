from typing import List
import math


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        n = len(points)
        if angle == 360:
            return n
        angle = angle / 180 * math.pi
        pi = math.pi
        x, y = location
        angles = []
        always = 0
        for i, (p, q) in enumerate(points):
            if p == x and q == y:
                always += 1
            else:
                a = math.atan2(q-y, p-x)
                angles.append(a if a >= 0 else a + 2*pi)
        # for i, (p, q) in enumerate(points):
        #     dx, dy = p-x, q-y
        #     if dy > 0:
        #         if dx > 0:
        #             a = math.atan(dy / dx)
        #         elif dx == 0:
        #             a = pi / 2
        #         else:
        #             a = pi - math.atan(dy/-dx)
        #     elif dy == 0:
        #         if dx > 0:
        #             a = 0
        #         elif dx == 0:
        #             always += 1
        #             continue
        #         else:
        #             a = pi
        #     else:
        #         if dx < 0:
        #             a = pi + math.atan(dy / dx)
        #         elif dx == 0:
        #             a = 1.5 * pi
        #         else:
        #             a = 2*pi - math.atan(-dy /dx)
        angles.sort()
        m = len(angles)
        r = 0
        ans = 0
        for l in range(m):
            while r < l + m:
                if r >= m:
                    tmp = 2*pi + angles[r%m]
                else:
                    tmp = angles[r]
                if tmp - angles[l] <= angle:
                    r += 1
                else:
                    break
            ans = max(ans, r-l)
        
        return ans + always

points = [[41,7],[22,94],[90,53],[94,54],[58,50],[51,96],[87,88],[55,98],[65,62],[36,47],[91,61],[15,41],[31,94],[82,80],[42,73],[79,6],[45,4]]
angle =  17
loc =    [6,84]
print(Solution().visiblePoints(points, angle, loc))