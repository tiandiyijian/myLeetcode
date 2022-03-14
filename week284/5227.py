from typing import List


class Solution:

    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return nums[0]
        if k == 1:
            if n == 1:
                return -1
            return nums[1]
        if k < n:
            return max(max(nums[0:k - 1]), nums[k])
        if k == n:
            return max(nums[0:k - 1])
        if k > n:
            if n == 1:
                if k & 1 == 1:
                    return -1
                else:
                    return nums[0]
            return max(nums)