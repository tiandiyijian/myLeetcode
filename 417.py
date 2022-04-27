from collections import deque
from typing import List


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        def bfs(q: deque):
            vis = set(q)
            while q:
                x, y = q.popleft()
                height = heights[x][y]
                for i in range(4):
                    new_x, new_y = x + dx[i], y + dy[i]
                    if 0 <= new_x < m and 0 <= new_y < n and not (
                            new_x, new_y) in vis:
                        if heights[new_x][new_y] >= height:
                            q.append((new_x, new_y))
                            vis.add((new_x, new_y))
            return vis

        q_pacfic = deque([(i, 0) for i in range(m)] + [(0, i) for i in range(n)])
        q_atlantic = deque([(i, n-1) for i in range(m)] + [(m-1, i) for i in range(n)])

        q_pacfic = bfs(q_pacfic)
        q_atlantic = bfs(q_atlantic)

        return [[x, y] for x, y in q_pacfic & q_atlantic]
