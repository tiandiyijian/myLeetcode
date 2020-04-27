from typing import List
import copy
import collections

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        i = 0
        rows, cols = len(matrix), len(matrix[0])
        # distance = [[0] * cols for _ in range(rows)]
        distance = copy.deepcopy(matrix)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        flag = True
        while flag:
            flag = False
            for r in range(rows):
                for c in range(cols):
                    if matrix[r][c] == 1:
                        if distance[r][c] < 0 and -distance[r][c] <= i:
                            continue
                        for x, y in directions:
                            p = r + x
                            q = c + y
                            if 0 <= p < rows and 0 <= q < cols and distance[p][q] == -i:
                                distance[r][c] = -(i + 1)
                                flag = True
                                break
            i += 1
            # print(distance)
        for r in range(rows):
            for c in range(cols):
                distance[r][c] = -distance[r][c]
        return distance

    def updateMatrix1(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        distance = [[None] * cols for _ in range(rows)]
        # distance = copy.deepcopy(matrix)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        q = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    q.appendleft((i, j))
                    distance[i][j] = 0
        dis = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and distance[nx][ny] is None:
                        q.appendleft((nx, ny))
                        distance[nx][ny] = dis + 1
            dis += 1
        return distance

if __name__ == "__main__":
    s = Solution()
    m = [[0,0,0],[0,1,0],[0,0,0]]
    m = [[0,0,0],[0,1,0],[1,1,1]]
    m = [[0,1,0],[0,1,0],[0,1,0]]
    print(s.updateMatrix1(m))