from typing import List


class Solution:

    def longestPath(self, parent: List[int], s: str) -> int:
        # 与其说是最长路径
        # 不如说是最长路径包含的节点数量
        # 可惜第三题看了太久今天又起得晚从11点才开始导致没时间交这题
        n = len(parent)
        child = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p >= 0:
                child[p].append(i)
        # print(child)
        longestPath = 0

        def dfs(i):
            # print(i)
            maxPath = secondPath = 1
            for j in child[i]:
                tmp = dfs(j)
                if s[j] != s[i]:
                    path = tmp + 1
                    if path >= maxPath:
                        maxPath, secondPath = path, maxPath
                    elif path > secondPath:
                        secondPath = path
            nonlocal longestPath
            longestPath = max(maxPath + secondPath - 1, longestPath)
            return maxPath

        dfs(0)
        return longestPath


p = [-1, 0, 0, 1, 1, 2]
s = "abacbe"

p = [-1, 0, 0, 0]
s = "aabc"

p = [-1, 0, 1]
s = "aab"
print(Solution().longestPath(p, s))
