from math import sqrt
from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        xmax = max(t[0] for t in towers)
        ymax = max(t[1] for t in towers)

        xc = yc = 0
        quality = 0
        for i in range(xmax + 1):
            for j in range(ymax + 1):
                tot_q = 0
                for x, y, q in towers:
                    d = sqrt((x - i) ** 2 + (y - j) ** 2)
                    if d <= radius:
                        tot_q += q // (1 + d)
                if tot_q > quality:
                    xc = i
                    yc = j
                    quality = tot_q

        return [xc, yc]
