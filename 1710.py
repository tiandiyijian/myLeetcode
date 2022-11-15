from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])

        ans = 0
        picked = 0
        for x in boxTypes:
            can_pick = min(truckSize - picked, x[0])
            ans += can_pick * x[1]
            picked += can_pick
            if picked == truckSize:
                break
        return ans
