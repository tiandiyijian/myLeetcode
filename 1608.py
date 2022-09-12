from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        for i in range(n):
            x = i + 1
            if nums[i] >= x and (x == n or nums[x] < x):
                return x

        return -1
