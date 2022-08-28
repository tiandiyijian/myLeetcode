from collections import deque
from typing import List


class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 关于怎么求树中最长路径：
        # 从任意节点出发到达离它最远的节点
        # 再从该节点到达离它最远的节点
        # 这两个节点间的路径就是最长路径
        
        # degrees = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            # degrees[a] += 1
            # degrees[b] += 1
            graph[a].append(b)
            graph[b].append(a)

        # for i in range(n):
        #     if degrees[i] == 1:
        #         break
        # print(i)
        q = deque([0])
        dists = [0] * n
        # pre = [-1] * n
        max_dist = 0
        while q:
            cur = q.pop()
            max_dist = dists[cur] + 1
            for j in graph[cur]:
                if j != 0 and dists[j] == 0:
                    dists[j] = max_dist
                    # pre[j] = cur
                    q.appendleft(j)

        start = cur
        q = deque([start])
        dists = [0] * n
        pre = [-1] * n
        max_dist = 0
        while q:
            cur = q.pop()
            max_dist = dists[cur] + 1
            for j in graph[cur]:
                if j != start and dists[j] == 0:
                    dists[j] = max_dist
                    pre[j] = cur
                    q.appendleft(j)
        max_dist -= 1
        # print(max_dist, dists)
        if max_dist & 1 == 0:
            mid = max_dist >> 1
            while mid > 0:
                cur = pre[cur]
                mid -= 1
            return [cur]
        else:
            mid = max_dist >> 1
            while mid > 0:
                cur = pre[cur]
                mid -= 1
            return [cur, pre[cur]]
