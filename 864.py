from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = 0
        pos = (-1, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    pos = (i, j)
                elif grid[i][j].islower():
                    keys += 1

        target = (1 << keys) - 1
        visited = {(*pos, 0, 0)}  # x, y, keys, locks
        # 其实也可以把锁的状态去掉
        # 有钥匙就可以通过没有就不行
        # 锁的状态没用
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(*pos, 0, 0, 0)])
        while q:
            x, y, s1, s2, step = q.popleft()
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] != '#':
                    cur = grid[new_x][new_y]
                    if cur.islower():
                        # if s1 & (1 << (ord(cur) - ord('a'))) > 0:
                        #     continue
                        new_s1 = s1 | (1 << (ord(cur) - ord('a')))
                        if new_s1 == target:
                            return step + 1
                        nxt = (new_x, new_y, new_s1, s2)
                        if nxt in visited:
                            continue
                        visited.add(nxt)
                        q.append((*nxt, step + 1))
                    elif cur.isupper():
                        if s1 & (1 << (ord(cur) - ord('A'))) > 0:
                            new_s2 = s2 | (1 << (ord(cur) - ord('A')))
                            nxt = (new_x, new_y, s1, new_s2)
                            if nxt in visited:
                                continue
                            visited.add(nxt)
                            q.append((*nxt, step + 1))
                    else:
                        nxt = (new_x, new_y, s1, s2)
                        if nxt in visited:
                            continue
                        visited.add(nxt)
                        q.append((*nxt, step + 1))

        return -1
