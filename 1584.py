#
# @lc app=leetcode.cn id=1584 lang=python3
#
# [1584] 连接所有点的最小费用
#
import collections
import heapq
from typing import List


# @lc code=start
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDistance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])

        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                dis = manhattanDistance(points[i], points[j])
                edges.append((dis, i, j))

        heapq.heapify(edges)
        UF = UnionFind(n)
        edge_count = 0
        ans = 0
        while edge_count < n - 1:
            dis, i, j = heapq.heappop(edges)
            fi, fj = UF.find(i), UF.find(j)
            if fi == fj:
                continue
            ans += dis
            UF.union(i, j)
            edge_count += 1
        return ans
# @lc code=end
