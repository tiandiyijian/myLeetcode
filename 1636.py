from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnter = Counter(nums)
        return sorted(nums, key=lambda x: (cnter[x], -x))
