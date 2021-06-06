from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # n = len(nums)
        # pre_sum = [0]*(n+1)
        # for i, num in enumerate(nums):
        #     pre_sum[i+1] = pre_sum[i] + nums[i]
        mp = {0: -1}
        ans = 0
        pre_sum = 0
        for i, val in enumerate(nums):
            pre_sum += 1 if val == 1 else -1
            if (ix := mp.get(pre_sum, -2)) >= -1:
                ans = max(ans, i - ix)
            else:
                mp[pre_sum] = i
        return ans
