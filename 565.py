from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visit = set()

        def dfs(i):
            if i in visit:
                return 0
            visit.add(i)
            return 1 + dfs(nums[i])

        return max(dfs(i) for i in range(len(nums)))
