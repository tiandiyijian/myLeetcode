from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        n = len(isConnected)
        visited = set()

        def dfs(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and i != j and j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                ans += 1
                dfs(i)
            if len(visited) == n:
                return ans

        # return ans


if __name__ == "__main__":
    s = Solution()
    m = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(s.findCircleNum(m))
