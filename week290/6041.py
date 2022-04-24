import operator
from typing import List


class Solution:

    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for i in range(1, len(nums)):
            ans &= set(nums[i])
        return sorted(ans)