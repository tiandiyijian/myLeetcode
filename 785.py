import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                q = collections.deque([i])
                color[i] = 1
                while q:
                    node = q.pop()
                    color_neighbor = 1 if color[node] == 2 else 2
                    for nei in graph[node]:
                        if color[nei] == 0:
                            q.appendleft(nei)
                            color[nei] = color_neighbor
                        elif color[nei] != color_neighbor:
                            print(node, nei)
                            return False
        return True

if __name__ == "__main__":
    s = Solution()
    g = [[1,3],[0,2],[1,3],[0,2]]
    print(s.isBipartite(g))
