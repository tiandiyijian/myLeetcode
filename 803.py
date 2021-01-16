from typing import List


class UnionFind:
    def __init__(self, n):
        self.f = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if x != self.f[x]:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

    def getSize(self, i):
        return self.rank[self.find(i)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # 正序敲砖，可以反过来看，即倒序添加
        # 看每一次添加一块砖能有多少块砖连到顶部就是敲掉这块砖时消失的砖的数量（注意减去本身）
        m, n = len(grid), len(grid[0])
        size = m * n
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def getIdx(i, j): return i * n + j

        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = -1
        # print(grid)

        UF = UnionFind(size + 1)

        for i in range(n):
            if grid[0][i] == 1:
                UF.union(i, size)

        # print(UF.f)
        # print(UF.rank)

        for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 只考虑上边和左边
                    if grid[i-1][j] == 1:
                        UF.union(getIdx(i-1, j), getIdx(i, j))
                    if j > 0 and grid[i][j-1] == 1:
                        UF.union(getIdx(i, j-1), getIdx(i, j))

        hit_len = len(hits)
        ans = [0] * hit_len
        for i in range(hit_len - 1, -1, -1):
            x = hits[i][0]
            y = hits[i][1]
            if grid[x][y] == 0:
                continue
            pre_size = UF.getSize(size)
            # print(pre_size)
            if x == 0:
                UF.union(y, size)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    UF.union(getIdx(x, y), getIdx(nx, ny))
            current_size = UF.getSize(size)
            ans[i] = max(0, current_size - pre_size - 1)
            grid[x][y] = 1
        return ans


if __name__ == "__main__":
    s = Solution()
    grid = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    hits = [[0, 2], [2, 0], [0, 1], [1, 2]]
    print(s.hitBricks(grid, hits))
