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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        if m * n < 2:
            return 0
        edges = []
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if i < m - 1:
                    edges.append(
                        (idx, idx + n, abs(heights[i][j] - heights[i+1][j])))
                if j < n - 1:
                    edges.append(
                        (idx, idx + 1, abs(heights[i][j] - heights[i][j+1])))
        edges.sort(key=lambda x: x[2])
        uf = UnionFind(m * n)
        for a, b, cost in edges:
            uf.union(a, b)
            if uf.isConnected(0, m * n - 1):
                return cost


if __name__ == "__main__":
    s = Solution()
    print()
