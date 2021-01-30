from typing import List


class UnionFind:
    def __init__(self, n):
        self.f = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.f[fy] = fx
        self.rank[fx] += self.rank[fy]

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 其实这道题中`grid[i][j]` 是`[0, ..., N*N - 1]` 的排列
        # 所以可以不用排序，直接用数组存下来就行了，索引表示高度，值表示坐标
        n = len(grid)
        edges = []
        for i in range(n):
            for j in range(n):
                idx = i * n + j
                if i < n - 1:
                    edges.append(
                        (idx, idx + n, max(grid[i][j], grid[i+1][j])))
                if j < n - 1:
                    edges.append(
                        (idx, idx + 1, max(grid[i][j], grid[i][j+1])))
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(n * n)
        for a, b, cost in edges:
            uf.union(a, b)
            if uf.isConnected(0, n * n - 1):
                return cost


if __name__ == "__main__":
    s = Solution()
    print()
