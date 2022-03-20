from typing import List


class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = 1
        while i < n:
            prev = nums[i - 1]
            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1
            if i == n - 1:
                break
            post = nums[i + 1]
            if (prev > nums[i] and post > nums[i]) or (prev < nums[i]
                                                       and post < nums[i]):
                ans += 1
            i += 1

        return ans
