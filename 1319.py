#
# @lc app=leetcode.cn id=1319 lang=python3
#
# [1319] 连通网络的操作次数
#
from typing import List



# @lc code=start
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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 答案就是连通分支的数量减1
        if n > len(connections) + 1:
            return -1
        UF = UnionFind(n)
        for a, b in connections:
            UF.union(a, b)
        return UF.count - 1
# @lc code=end

