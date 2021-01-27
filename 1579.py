from copy import deepcopy
from typing import List


class UnionFind:
    def __init__(self, n):
        """
        Union-find
        """
        self.count = n
        n += 1
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
            return True
        if self.rank[fa] > self.rank[fb]:
            fa, fb = fb, fa
        self.f[fa] = fb
        self.rank[fb] += self.rank[fa]
        self.count -= 1
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        ans = 0
        ua = UnionFind(n)
        i = 0
        m = len(edges)
        while i < m and edges[i][0] == 3:
            if ua.union(edges[i][1], edges[i][2]):
                ans += 1
            i += 1
        ub = deepcopy(ua)
        while i < m and edges[i][0] == 2:
            if ub.union(edges[i][1], edges[i][2]):
                ans += 1
            i += 1
        while i < m and edges[i][0] == 1:
            if ua.union(edges[i][1], edges[i][2]):
                ans += 1
            i += 1
        return -1 if (ua.count > 1 or ub.count > 1) else ans


if __name__ == "__main__":
    s = Solution()
    n = 4
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    print(s.maxNumEdgesToRemove(n, edges))
