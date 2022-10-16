from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n <= 2 or len(dislikes) <= 2:
            return True

        color = [0] * n
        g = [[] for _ in range(n)]
        for a, b in dislikes:
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)

        def dfs(cur, c):
            if color[cur] > 0:
                if c > 0:
                    return color[cur] == c
                else:
                    return True
            if c == 0:
                c = 1
            color[cur] = c
            return all(dfs(nei, 3 - c) for nei in g[cur])

        return all(dfs(nei, 0) for nei in range(n))
