from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island1, island2 = set(), set()
        neighbors1, neighbors2 = set(), set()
        # 失了智，刚开始想搞个双向BFS然后又感觉没必要

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(i, j, island, nei):
            for k in range(4):
                new_x = i + dx[k]
                new_y = j + dy[k]
                if 0 <= new_x < m and 0 <= new_y < n:
                    if grid[new_x][new_y] == 1:
                        if (new_x, new_y) not in island:
                            island.add((new_x, new_y))
                            dfs(new_x, new_y, island, nei)
                    else:
                        nei.add((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island1.add((i, j))
                    dfs(i, j, island1, neighbors1)
                    break
            else:
                continue
            break

        q = list(neighbors1)
        neighbors1 |= island1
        step = 0
        while True:
            if not q:
                return -1
            new_q = []
            for pos in q:
                i, j = pos
                for k in range(4):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if (
                        0 <= new_x < m
                        and 0 <= new_y < n
                        and (new_x, new_y) not in neighbors1
                    ):
                        if grid[new_x][new_y] == 1:
                            return step + 1
                        new_q.append((new_x, new_y))
                        neighbors1.add((new_x, new_y))
            q = new_q
            step += 1


g = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
]

print(Solution().shortestBridge(g))
