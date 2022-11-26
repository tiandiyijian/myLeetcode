from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, cnt in edges:
            g[u].append((v, cnt + 1))
            g[v].append((u, cnt + 1))  # 建图

        dist = [inf] * n
        dist[0] = 0
        h = [(0, 0)]
        while h:
            d, x = heappop(h)
            if d > dist[x]:
                continue
            for y, wt in g[x]:
                if (new_d := dist[x] + wt) < dist[y]:
                    dist[y] = new_d
                    heappush(h, (new_d, y))

        ans = sum(d <= maxMoves for d in dist)
        for u, v, cnt in edges:
            ans += min(max(maxMoves - dist[u], 0) + max(maxMoves - dist[v], 0), cnt)

        return ans
