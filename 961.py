from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return max(Counter(nums).items(), key = lambda x: x[1])[0]
        