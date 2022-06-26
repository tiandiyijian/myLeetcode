from functools import reduce
from operator import xor
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # 参考https://leetcode.cn/problems/minimum-score-after-removals-on-a-tree/solution/by-tsreaper-4fdj/
        ans = float('inf')
        n = len(nums)
        all_x = reduce(xor, nums)
        part23 = 0

        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(start, father, ban):
            ret = nums[start]
            for nei in g[start]:
                if nei != ban and nei != father:
                    ret ^= dfs(nei, start, ban)
            return ret

        def dfs2(start, father, ban):
            ret = nums[start]
            nonlocal ans
            for nei in g[start]:
                if nei != father and nei != ban:
                    part3 = dfs2(nei, start, ban)
                    ret ^= part3
                    part2 = part23 ^ part3
                    part1 = all_x ^ part23
                    tmp = [part1, part2, part3]
                    ans = min(ans, max(tmp) - min(tmp))
            return ret

        for i in range(n):
            for j in g[i]:
                part23 = dfs(i, -1, j)
                dfs2(i, -1, j)

        return ans
