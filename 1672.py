from typing import List


class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(wealth) for wealth in accounts)