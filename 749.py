from collections import deque
from typing import List


class Solution:
    def containVirus0(self, isInfected: List[List[int]]) -> int:
        # CV了
        m, n = len(isInfected), len(isInfected[0])
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        def bfs(x, y, global_visit):
            size = 1
            q = deque([(x, y)])
            visit = {(x, y)}
            global_visit.add((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < m and 0 <= new_y < n and isInfected[new_x][new_y] == 1:
                        if (tmp := (new_x, new_y)) not in visit:
                            q.append(tmp)
                            visit.add(tmp)
                            global_visit.add(tmp)
                            size += 1
            return size
        
        def diffuse(x, y):
            q = deque([(x, y)])
            visit = {(x, y)}
            area = set(get_nei(x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < m and 0 <= new_y < n and isInfected[new_x][new_y] == 1:
                        if (tmp := (new_x, new_y)) not in visit:
                            q.append(tmp)
                            visit.add(tmp)
                            area = area.union(get_nei(*tmp))
            for i, j in area:
                isInfected[i][j] = 1
        
        def get_nei(x, y):
            res = []
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < m and 0 <= new_y < n and isInfected[new_x][new_y] == 0:
                    res.append((new_x, new_y))
            return res
        
        def wall(x, y):
            q = deque([(x, y)])
            visit = {(x, y)}
            walles = set(get_wall(x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < m and 0 <= new_y < n and isInfected[new_x][new_y] == 1:
                        if (tmp := (new_x, new_y)) not in visit:
                            q.append(tmp)
                            visit.add(tmp)
                            walles = walles.union(get_wall(*tmp))            
        
        def get_wall(x, y):
            res = []
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < m and 0 <= new_y < n and isInfected[new_x][new_y] == 0:
                    res.append((new_x, new_y))
            return res
        
        while True:
            global_visit = set()
            sizes = {}
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in global_visit:
                        cur_size = bfs(i, j, global_visit)
                        sizes[(i, j)] = cur_size
    
    def containVirus(self, isInfected: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m, n = len(isInfected), len(isInfected[0])
        ans = 0

        while True:
            # 在BFS的同时标记当前连通分支并记录它的邻居和需要安装的防火墙数量
            # 然后找到邻居数最小的那个, 再把标记恢复回来
            neighbors, firewalls = list(), list()
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()
                        firewall, idx = 0, len(neighbors) + 1
                        isInfected[i][j] = -idx

                        while q:
                            x, y = q.popleft()
                            for d in range(4):
                                nx, ny = x + dirs[d][0], y + dirs[d][1]
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 1:
                                        q.append((nx, ny))
                                        isInfected[nx][ny] = -idx
                                    elif isInfected[nx][ny] == 0:
                                        firewall += 1
                                        neighbor.add((nx, ny))
                        
                        neighbors.append(neighbor)
                        firewalls.append(firewall)
            
            if not neighbors:
                break

            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i
                
            ans += firewalls[idx]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2
            
            for i, neighbor in enumerate(neighbors):
                if i != idx:
                    for x, y in neighbor:
                        isInfected[x][y] = 1
            
            if len(neighbors) == 1:
                break
        
        return ans    