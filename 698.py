from functools import cache
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, m = divmod(sum(nums), k)
        if m != 0:
            return False

        n = len(nums)
        nums.sort()
        if nums[-1] > target:
            return False

        @cache
        def dfs(curSum, state):
            if state == 0:
                return True

            if curSum == target:
                curSum = 0

            for j in range(n):
                if curSum + nums[j] > target:
                    break
                if state & (1 << j) > 0 and curSum + nums[j] <= target:
                    if dfs(curSum + nums[j], state ^ (1 << j)):
                        return True
                    if curSum == 0:
                        # 如果当前集合还没有值，那么随便挑选一个值都得保证能够成功才能成功
                        return False

            return False

        state = (1 << n) - 1
        return dfs(0, state)
