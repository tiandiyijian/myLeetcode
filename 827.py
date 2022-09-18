from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1

        islands = {}
        islands_size = defaultdict(int)
        islands_size[-1] = 0
        cur_id = 0

        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]

        def dfs(x, y, cur_id):
            # if (x, y) in islands:
            #     return
            islands[(x, y)] = cur_id
            islands_size[cur_id] += 1
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if (
                    0 <= new_x < n
                    and 0 <= new_y < n
                    and grid[new_x][new_y] == 1
                    and (new_x, new_y) not in islands
                ):
                    dfs(new_x, new_y, cur_id)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in islands:
                    dfs(i, j, cur_id)
                    cur_id += 1

        # print(islands)
        # print(islands_size)
        ans = min(max(islands_size.values()) + 1, n ** 2)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for k in range(4):
                        new_x = i + dx[k]
                        new_y = j + dy[k]
                        if (
                            0 <= new_x < n
                            and 0 <= new_y < n
                            and (new_x, new_y) in islands
                        ):
                            neighbors.add(islands[(new_x, new_y)])

                    sizes = [islands_size[i] for i in neighbors]
                    ans = max(sum(sizes) + 1, ans)

        return ans
