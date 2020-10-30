from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            nonlocal ans, visited
            visited.add((i, j))
            for dx, dy in direction:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] == 1 and (x, y) not in visited:
                        dfs(x, y)
                    elif grid[x][y] == 0:
                        ans += 1
                else:
                    ans += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans


if __name__ == "__main__":
    s = Solution()
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(grid))
