from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        pre_count, pre_val = 0, None
        cur_count, cur_val = 1, nums[0]
        ans = 0
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cur_count += 1
            else:
                if pre_val == cur_val - 1:
                    ans = max(ans, pre_count + cur_count)
                pre_count = cur_count
                pre_val = cur_val
                cur_count = 1
                cur_val = nums[i]
        if pre_val == cur_val - 1:
            ans = max(ans, pre_count + cur_count)
        return ans
