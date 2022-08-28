from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum = min(nums)
        return sum(x - minNum for x in nums)