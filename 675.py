from collections import deque
from typing import List, Tuple


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(start: Tuple, end: Tuple):
            visited = {start}
            q = deque([(start, 0)])
            while q:
                cur = q.popleft()
                if cur[0] == end:
                    return cur[1]
                cur_x, cur_y = cur[0]
                step = cur[1]
                for i in range(4):
                    new_x, new_y = cur_x + dx[i], cur_y + dy[i]
                    if 0 <= new_x < m and 0 <= new_y < n and forest[new_x][new_y] > 0:
                        next_pos = (new_x, new_y)
                        if next_pos not in visited:
                            q.append((next_pos, step+1))
                            visited.add(next_pos)
            return -1
        
        trees = [(i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1]
        trees.sort(key=lambda x:forest[x[0]][x[1]])
        cur = (0, 0)
        ans = 0
        for tree in trees:
            d = bfs(cur, tree)
            # print(d, cur, tree)
            if d < 0:
                return -1
            ans += d
            cur = tree
        return ans