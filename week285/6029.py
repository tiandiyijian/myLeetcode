from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_point = -1
        ans = []
        
        def helper(i, numArrows, point, points):
            if numArrows < 0:
                return
            if i == 0:
                nonlocal max_point, ans
                if point > max_point:
                    max_point = point
                    ans = points
                return
            helper(i-1, numArrows - aliceArrows[i] - 1, point + i, points + [aliceArrows[i] + 1])
            helper(i-1, numArrows, point, points + [0])
        
        helper(11, numArrows, 0, [])
        return [numArrows - sum(ans)] + ans[::-1]