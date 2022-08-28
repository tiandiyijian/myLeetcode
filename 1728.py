from functools import lru_cache
from typing import List


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        max_status = 2*m*n
        # max_status = 1000
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        @lru_cache(None)
        def dfs(mx, my, cx, cy, round):
            # 极大极小博弈
            # 博弈的时候双方都要选择最优策略
            
            if round > max_status:
                return False
            
            if (mx == cx and my == cy) or grid[cx][cy] == 'F':
                return False
            
            if grid[mx][my] == 'F':
                return True
            
            jump = mouseJump if round & 1 == 0 else catJump

            for i in range(4):
                for step in range(0, jump + 1):
                    # 也可以不移动, 对应被墙卡死的情况, range要从0开始
                    # 如果猫被卡死老鼠也被卡死的话最后还是猫赢
                    # 如果不加上这一个逻辑的话这个双重循环里的递归不会被执行(全部撞墙)
                    # 那么直接跳到该函数最后一行导致逻辑出错
                    # 比如说这个样例
                    # ["####.##",".#C#F#.","######.","##M.###"]
                    new_x = (mx if round & 1 == 0 else cx) + dx[i] * step
                    new_y = (my if round & 1 == 0 else cy) + dy[i] * step
                    if not (0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] != '#'):
                        # 撞墙或出界直接break
                        # 因为step变大的话还是撞墙(不能越过墙)或出界
                        break
                    if round & 1 == 0 and dfs(new_x, new_y, cx, cy, round + 1):
                        # mouse最优策略
                        print(new_x, new_y, cx, cy, round + 1)
                        return True
                    elif round & 1 and not dfs(mx, my, new_x, new_y, round + 1):
                        # cat最优策略
                        return False
            
            # print(mx, my, cx, cy, round, False if round & 1 == 0 else True)
            return False if round & 1 == 0 else True

        for i in range(m):
            for j in range(n):
                match grid[i][j]:
                    case 'C':
                        cx, cy = i, j
                    case 'M':
                        mx, my = i, j

        return dfs(mx, my, cx, cy, 0)


grid = ["####.##",".#C#F#.","######.","##M.###"]
cj = 3
mj = 6
print(Solution().canMouseWin(grid, cj, mj))
    