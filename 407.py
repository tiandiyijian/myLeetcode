import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visit = [[False] * n for _ in range(m)]
        
        pq = []
        for i in range(m):
            heapq.heappush(pq, (heightMap[i][0], i * n))
            heapq.heappush(pq, (heightMap[i][n-1], i * n + n - 1))
            visit[i][0] = True
            visit[i][n-1] = True
        for j in range(1, n-1):
            heapq.heappush(pq, (heightMap[0][j], j))
            heapq.heappush(pq, (heightMap[m-1][j], (m-1)*n + j))
            visit[0][j] = 1
            visit[m-1][j] = 1
        
        ans = 0
        dir = [-1, 0, 1, 0, -1]
        while pq:
            min_height, pos = heapq.heappop(pq)
            nx = pos // n
            ny = pos % n
            for i in range(4):
                x = nx + dir[i]
                y = ny + dir[i+1]
                if 0 <= x < m and 0 <= y < n and not visit[x][y]:
                    if heightMap[x][y] < min_height:
                        ans += min_height - heightMap[x][y]
                    visit[x][y] = True
                    heapq.heappush(pq, (max(heightMap[x][y], min_height), x * n + y))
        return ans
