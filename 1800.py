from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        n = len(nums)

        i = 0
        while i < n:
            cur = nums[i]
            j = i + 1
            while j < n and nums[j] > nums[j - 1]:
                cur += nums[j]
                j += 1
            ans = max(ans, cur)
            i = j

        return ans
