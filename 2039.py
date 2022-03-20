from collections import deque
from typing import List


class Solution:

    def networkBecomesIdle(self, edges: List[List[int]],
                           patience: List[int]) -> int:
        n = len(patience)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # min_dist = [float('inf')] * n
        q = deque([(0, 0)])
        max_time = 0
        visit = {0}
        while q:
            node, path = q.popleft()
            max_time = max(
                max_time, ((path * 2 - 1) // patience[node]) * patience[node] +
                path * 2) if node != 0 else 0
            # min_dist[node] = path
            for nei in graph[node]:
                if nei not in visit:
                    q.append((nei, path + 1))
                    visit.add(nei)

        # max_time = 0
        # for i in range(1, n):
        #     return_time = min_dist[i] * 2
        #     if return_time % patience[i] == 0:
        #         last_send_time = return_time - patience[i]
        #     else:
        #         last_send_time = return_time - (return_time % patience[i])
        #     max_time = max(max_time, last_send_time + return_time)

        return max_time + 1