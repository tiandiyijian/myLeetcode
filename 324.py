from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # 有点难想
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
