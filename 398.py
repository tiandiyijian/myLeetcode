from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        ans = 0
        for i, num in enumerate(self.nums):
            if num == target:
                if randint(0, cnt) == 0:
                    ans = i
                cnt += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)