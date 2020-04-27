from typing import List
import collections
from copy import deepcopy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def checkGrid():
            for row in grid:
                for col in row:
                    if col == 1:
                        return False
            return True
        
        def isInGrid(i, j):
            return 0 <= i < rows and 0<= j < cols and grid[i][j] == 1

        def expandGrid():
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if isInGrid(i-1, j):
                            tmp[i-1][j] = 2
                        if isInGrid(i+1, j):
                            tmp[i+1][j] = 2
                        if isInGrid(i, j-1):
                            tmp[i][j-1] = 2
                        if isInGrid(i, j+1):
                            tmp[i][j+1] = 2
                    elif grid[i][j] == 1:
                        count += 1
            return count

        min_minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        old_count = 0
        while True:
            if checkGrid():
                return min_minutes
            tmp = deepcopy(grid)
            new_count = expandGrid()
            if old_count == new_count:
                if new_count == 0:
                    return min_minutes
                else:
                    return -1
            old_count = new_count
            grid = tmp
            min_minutes += 1
            print(grid)

    def orangesRotting1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0, 1], [0, -1]]
        queue = collections.deque()
        fresh = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.appendleft((r, c))
                elif grid[r][c] == 1:
                    fresh = True
        if not queue:
            return -1 if fresh else 0
        d = 0
        while queue:
            print(queue)
            length = len(queue)
            for _ in range(length):
                r, c = queue.pop()
                for direction in directions:
                    r_new, c_new = r + direction[0], c + direction[1]
                    if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new] == 1:
                        grid[r_new][c_new] = 2
                        queue.appendleft((r_new, c_new))
            d += 1
        if any(1 in row for row in grid):
            return -1
        return d - 1


if __name__ == "__main__":
    s = Solution()
    grid = [[0]]
    print(s.orangesRotting1(grid))
