from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                ans[i][j] = 0
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        ans[i][j] = max(ans[i][j], grid[p][q])
        
        return ans