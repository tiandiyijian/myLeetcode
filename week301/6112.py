from math import ceil
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 每次至多接某一类型的水一次，所以总时长至少为 max(amount)
        # 每次至多接两杯水，所以总时长至少为 sum(amount)/2
        return max(max(amount), ceil(sum(amount) / 2))
