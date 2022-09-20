from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, m = divmod(sum(nums), k)
        if m != 0:
            return False

        n = len(nums)
        ans = False

        @cache
        def dfs(i, curSum, state):
            nonlocal ans
            if ans:
                return

            if curSum == target:
                i += 1
                curSum = 0

            if i == k:
                ans = True
                return

            for j in range(n):
                if state & (1 << j) > 0 and curSum + nums[j] <= target:
                    dfs(i, curSum + nums[j], state ^ (1 << j))

        state = (1 << n) - 1
        dfs(0, 0, state)
        return ans
