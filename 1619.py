import math
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        cnt = n // 20
        arr.sort()

        return sum(arr[cnt:-cnt]) / (n - 2 * cnt)
