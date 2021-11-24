from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(*left, *(n - x for x in right), 0)

s = Solution()
print(s.getLastMoment(1000, [0], []))