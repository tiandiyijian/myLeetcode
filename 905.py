from typing import List


class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            while l < n and nums[l] & 1 == 0:
                l += 1
            while r > 0 and nums[r] & 1 == 1:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            # print(l, r, nums)
        return nums