from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if nums[-1] > nums[0]:
                    return False
                for j in range(i + 1, n):
                    if nums[j] < nums[j - 1]:
                        return False

        return True
