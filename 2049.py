from typing import List


class Solution:

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        sons = [[] for _ in range(n)]
        for i in range(1, n):
            sons[parents[i]].append(i)

        max_score = 0
        ans = 0

        def dfs(i):
            if not sons[i]:
                score = n - 1
                size = 1
            elif len(sons[i]) == 1:
                son_size = dfs(sons[i][0])
                score = son_size
                if n - son_size - 1 > 1:
                    score *= n - son_size - 1
                size = son_size + 1
            else:
                size1, size2 = dfs(sons[i][0]), dfs(sons[i][1])
                score = size1 * size2
                left = n - size1 - size2 - 1
                if left > 1:
                    score *= left
                size = size1 + size2 + 1
            # print(i, score, size)
            nonlocal max_score, ans
            if score > max_score:
                max_score = score
                ans = 1
            elif score == max_score:
                ans += 1
            return size

        dfs(0)
        return ans


print(Solution().countHighestScoreNodes([-1, 3, 3, 5, 7, 6, 0, 0]))
