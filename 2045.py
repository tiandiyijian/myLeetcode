from collections import deque


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        neighbor = [[] for _ in range(n+1)]
        for [a, b] in edges:
            neighbor[a].append(b)
            neighbor[b].append(a)
        dist = [[float('inf')] * 2 for _ in range(n+1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            p = q.popleft()
            for y in neighbor[p[0]]:
                d = p[1] + 1
                if d < dist[y][0]:
                    dist[y][1] = dist[y][0]
                    dist[y][0] = d
                    q.append((y, d))
                elif dist[y][0] < d < dist[y][1]:
                    dist[y][1] = d
                    q.append((y, d))
        total_time = 0
        for i in range(dist[n][1]):
            tmp = total_time % (2 * change)
            if tmp < change:
                total_time += time
            else:
                total_time += (2 * change - tmp + time)
        return total_time
