from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        pre_max = cur_max = nums[0]
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] < pre_max:
                pos = i
                pre_max = cur_max
            else:
                cur_max = max(cur_max, nums[i])
        return pos + 1
