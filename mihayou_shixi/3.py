# coding=utf-8
# 记录状态的广度优先搜索

import sys
from collections import deque

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split())
    map = [''] * n
    ans = 0
    x, y = -1, -1
    for i in range(n):
        line = sys.stdin.readline().strip()
        if x == -1 and 'm' in line:
            x = i
            y = line.index('m')
        map[i] = line

    visit = set((x, y, False, False))
    q = deque([(0, x, y, False, False)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    find = False
    while q:
        cur = q.popleft()
        path, i, j, hasFlower, hasMeat = cur
        for k in range(4):
            new_x = i + dx[k]
            new_y = j + dy[k]
            if 0 <= new_x < n and 0 <= new_y < m and map[new_x][new_y] != 'B':
                if hasFlower and hasMeat and map[new_x][new_y] == '^':
                    print(path + 1)
                    find = True
                    break
                newFlower = hasFlower
                newMeat = hasMeat
                if map[new_x][new_y] == '#':
                    newFlower = True
                elif map[new_x][new_y] == '$':
                    newMeat = True
                if (new_x, new_y, newFlower, newMeat) not in visit:
                    visit.add((new_x, new_y, newFlower, newMeat))
                    q.append((path+1, new_x, new_y, newFlower, newMeat))
        if find:
            break
    if not find:
        print(-1)
