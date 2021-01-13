from typing import List


class UnionFind:
    def __init__(self, n):
        """
        Union-find
        """
        self.f = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.f[i] == i:
            return i
        self.f[i] = self.find(self.f[i])
        return self.f[i]

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)

        if fa == fb:
            return
        if self.rank[fa] > self.rank[fb]:
            fa, fb = fb, fa
        self.f[fa] = fb
        self.rank[fb] += self.rank[fa]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        for a, b in edges:
            fa = uf.find(a)
            fb = uf.find(b)
            if fa == fb:
                return [a, b]
            uf.union(a, b)


if __name__ == "__main__":
    s = Solution()
    edges = [[9, 10], [5, 8], [2, 6], [1, 5], [3, 8],
             [4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]
    print(s.findRedundantConnection(edges))
