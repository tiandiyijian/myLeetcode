from typing import List


class Solution:

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            r2 = r**2
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if (i, j) not in points and (i-x)**2 + (j-y)**2 <= r2:
                        points.add((i, j))
        
        return len(points)


print(Solution().countLatticePoints([[2,2,2],[3,4,1]]))