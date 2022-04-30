from typing import List


class Solution:

    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        avg = (minNum + maxNum) / 2
        if minNum + k >= avg and maxNum - k <= avg:
            return 0
        return maxNum - k - minNum - k