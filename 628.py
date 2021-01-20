#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
from typing import List


# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= 0 or nums[-1] <= 0:
            return nums[-1] * nums[-2] * nums[-3]
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
# @lc code=end
