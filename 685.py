from typing import List


class UnionFind:
    def __init__(self, n):
        self.ancestor = list(range(n))

    def union(self, i, j):
        self.ancestor[self.find(i)] = self.find(j)

    def find(self, i):
        if self.ancestor[i] != i:
            self.ancestor[i] = self.find(self.ancestor[i])
        return self.ancestor[i]


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        node_count = len(edges)
        uf = UnionFind(node_count + 1)
        parent = list(range(node_count + 1))
        conflict = -1
        cycle = -1
        for i, (n1, n2) in enumerate(edges):
            if parent[n2] != n2:  # 第一次扫描到的时候父节点肯定是自己
                conflict = i
            else:
                parent[n2] = n1
                if uf.find(n2) == uf.find(n1):
                    cycle = i
                else:
                    uf.union(n2, n1)
            # print(uf.ancestor)
            # print(cycle)
        if conflict < 0:
            return edges[cycle]
        else:
            conflictEdge = edges[conflict]
            if cycle >= 0:
                return [parent[conflictEdge[1]], conflictEdge[1]]
            else:
                return conflictEdge


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantDirectedConnection([[3,1],[2,1],[4,2],[1,4]]))
