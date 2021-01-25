from typing import List


class UnionFind:
    def __init__(self, n):
        self.f = list(range(n))
        self.rank = [1] * n
        self.count = n

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
        self.count -= 1


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m = len(grid)
        n = 4 * m * m
        UF = UnionFind(n)

        for i in range(m):
            for j in range(m):
                base_idx = 4 * (i * m + j)
                if grid[i][j] == ' ':
                    UF.union(base_idx, base_idx + 1)
                    UF.union(base_idx, base_idx + 2)
                    UF.union(base_idx, base_idx + 3)
                elif grid[i][j] == '/':
                    UF.union(base_idx, base_idx + 3)
                    UF.union(base_idx + 2, base_idx + 1)
                else:
                    UF.union(base_idx, base_idx + 1)
                    UF.union(base_idx + 2, base_idx + 3)

                if j + 1 < m:
                    UF.union(base_idx + 1, base_idx + 7)
                if i + 1 < m:
                    UF.union(base_idx + 2, base_idx + 4 * m)
        return UF.count


if __name__ == "__main__":
    s = Solution()
    print()
