import bisect
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
        # indices = [bisect.bisect_left(houses, x) for x in heaters]

        def judge(r):
            pre_right = -1
            for pos in heaters:
                left = bisect.bisect_left(houses, pos - r)
                right = bisect.bisect_right(houses, pos + r) - 1
                # print(left, right)
                if left > pre_right + 1:
                    return False
                pre_right = right
            return pre_right >= len(houses) - 1

        low, high = 0, max(houses[-1], heaters[0])
        # print(judge(8))
        while low < high:
            # print(low, high)
            mid = low + ((high - low) >> 1)
            if judge(mid):
                high = mid
            else:
                low = mid + 1
        return high


houses = [1, 5]
heaters = [10]
print(Solution().findRadius(houses, heaters))
