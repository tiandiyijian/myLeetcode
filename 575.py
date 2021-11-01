from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candySet = set(candyType)
        return min(len(candySet), len(candyType) >> 1)
