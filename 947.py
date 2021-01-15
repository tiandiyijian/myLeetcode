from typing import List


class UnionFind:
    def __init__(self):
        self.f = dict()
        self.rank = dict()
        self.count = 0
    
    def find(self, x: int) -> int:
        if x not in self.f:
            self.f[x] = x
            self.rank[x] = 1
            self.count += 1
            return x
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]
    
    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx
        self.count -= 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 每一行每一列都是连通的，所以只用考虑行号和列号即可
        # 每个连通分量可以删到只剩一个，所以求出连通分量的个数即可
        UF = UnionFind()
        for x, y in stones:
            UF.unionSet(x, y + 10000)
        return len(stones) - UF.count


if __name__ == "__main__":
    s = Solution()
    print()
