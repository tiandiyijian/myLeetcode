from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # global必须和local一样多

        post_min = nums[-1]
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] > post_min:
                # 不能有global
                return False
            post_min = min(post_min, nums[i + 1])

        return True
