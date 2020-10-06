from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        distSum = [0] * N
        size = [0] * N
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # print(graph)
        
        def dfs1(n, parent):
            print(n, parent)
            for node in graph[n]:
                if node == parent:
                    continue
                dfs1(node, n)
                size[n] += size[node]
                distSum[n] += distSum[node] + size[node]
            size[n] += 1

        def dfs2(n, parent):
            for node in graph[n]:
                if node == parent:
                    continue
                distSum[node] = distSum[n] - size[node] + N - size[node]
                dfs2(node, n)

        dfs1(0, -1)
        dfs2(0, -1)
        return distSum 


if __name__ == "__main__":
    s = Solution()
    print(s.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))