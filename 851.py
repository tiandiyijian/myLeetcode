from typing import List
from collections import deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        for a, b in richer:
            g[b].append(a)

        ans = [-1]*n

        def dfs(i):
            if ans[i] != -1:
                return
            ans[i] = i
            for j in g[i]:
                dfs(j)
                if quiet[ans[j]] < quiet[ans[i]]:
                    ans[i] = ans[j]

        for i in range(n):
            dfs(i)
        return ans

    def TopologicalSorting(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        inDegree = [0]*n
        g = [[] for _ in range(n)]
        for a, b in richer:
            g[a].append(b)
            inDegree[b] += 1

        ans = list(range(n))
        q = deque((i for i in range(n) if inDegree[i] == 0))
        while q:
            x = q.popleft()
            for y in g[x]:
                if quiet[ans[x]] < quiet[ans[y]]:
                    ans[y] = ans[x]
                inDegree[y] -= 1
                if inDegree[y] == 0:
                    q.append(y)
        return ans
