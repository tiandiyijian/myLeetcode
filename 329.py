from typing import List
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(matrix), len(matrix[0])
        
        @lru_cache(None)
        def dfs(i, j):
            tmp_max = 1
            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    tmp_max = max(tmp_max, dfs(x, y) + 1)
            return tmp_max

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == "__main__":
    s = Solution()
    m = [[9,9,4],[6,6,8],[2,1,1]]
    print(s.longestIncreasingPath(m))
