import sys
from typing import List


class Solution:
    def cherryPickup(self, grid: list) -> int:
        if not grid or not grid[0] or grid[0][0] == -1:
            return 0
        n = len(grid)
        dp = [[-sys.maxsize-1] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*n-1):  #t表示已走的步数，最多能走2*n-2步
            dp2 = [[-sys.maxsize-1] * n for _ in range(n)]
            for i in range(max(0, t-(n-1)), min(n-1, t)+1):  #i，j分别表示两个点的横坐标，则这两个点的纵坐标分别为t-i，t-j
                for j in range(max(0, t-(n-1)), min(n-1, t)+1):
                    if grid[i][t-i] == -1 or grid[j][t-j] == -1:
                        continue
                    val = grid[i][t-i]
                    if i != j:
                        val += grid[j][t-j]
                    #print(val, i, j)
                    dp2[i][j] = max(val + dp[pi][pj] for pi in (i, i-1) for pj in (j, j-1) if pi >= 0 and pj >= 0)
            dp = dp2
            #for i in dp:
            #   print(i)
        return max(0, dp[n-1][n-1])
    
    def cherryPickup1(self, grid: List[List[int]]) -> int:
        # 和19年的错误思路差不多, 代码倒是写得好看了一点
        n = len(grid)
        dp = [[[0, ''] for _ in range(n)] for _ in range(n)]
        C = -n*n

        dp[0][0][0] = 1 if grid[0][0] == 1 else 0
        for i in range(1, n):
            dp[0][i] = (
                [C, ''] if grid[0][i] == -1 else [dp[0][i - 1][0] + grid[0][i], 'left']
            )
            dp[i][0] = (
                [C, ''] if grid[i][0] == -1 else [dp[i - 1][0][0] + grid[i][0], 'up']
            )

        for i in range(1, n):
            for j in range(1, n):
                if grid[i][j] == -1:
                    dp[i][j][0] = C
                    continue
                if dp[i - 1][j][0] > dp[i][j - 1][0]:
                    dp[i][j] = [dp[i - 1][j][0] + grid[i][j], 'up']
                else:
                    dp[i][j] = [dp[i][j - 1][0] + grid[i][j], 'left']

        ans = dp[-1][-1][0]
        if ans <= 0:
            return 0
        # print(ans, dp)
        x = y = n - 1
        while x + y > 0:
            grid[x][y] = 0
            if dp[x][y][1] == 'left':
                y -= 1
            else:
                x -= 1

        dp2 = [[0] * n for _ in range(n)]
        for i in range(1, n):
            dp2[0][i] = 0 if grid[0][i] == -1 else grid[0][i] + dp2[0][i - 1]
            dp2[i][0] = 0 if grid[i][0] == -1 else grid[i][0] + dp2[i - 1][0]

        for i in range(1, n):
            for j in range(1, n):
                dp2[i][j] = (
                    C
                    if grid[i][j] == -1
                    else (grid[i][j] + max(dp2[i - 1][j], dp2[i][j - 1]))
                )

        return ans + dp2[-1][-1]
