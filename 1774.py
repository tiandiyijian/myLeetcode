from functools import cache
from math import inf
from typing import List


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        ans = -inf
        n = len(toppingCosts)

        @cache
        def dfs(i, cur):
            nonlocal ans
            if abs(cur - target) < abs(ans - target):
                ans = cur
            elif abs(cur - target) == abs(ans - target) and cur < ans:
                ans = cur

            if cur > target:
                return

            if i == n:
                return

            for j in range(3):
                dfs(i + 1, cur + j * toppingCosts[i])

        for bc in baseCosts:
            dfs(0, bc)

        return ans
