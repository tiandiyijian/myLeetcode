from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for pos in position:
            if pos & 1 == 0:
                even += 1
            else:
                odd += 1

        return min(odd, even)
