from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            ans += max(nums[i - 1] + 1 - nums[i], 0)
            nums[i] = max(nums[i], nums[i - 1] + 1)

        return ans
