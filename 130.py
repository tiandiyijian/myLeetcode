import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def neighbor(i, j):
            x = [0, 0, 1, -1]
            y = [-1, 1, 0, 0]
            for d in range(4):
                if 0 <= i + x[d] < m and 0 <= j + y[d] < n:
                    yield (i+x[d], j+y[d])
        
        def margin():
            x = y = 0
            while y < n:
                yield x, y
                y += 1
            y -= 1
            x += 1
            while x < m:
                yield x, y
                x += 1
            x -= 1
            y -= 1
            while y >= 0:
                yield x, y
                y -= 1
            y += 1
            x -= 1
            while x >= 1:
                yield x, y
                x -= 1

        for i, j in margin():
            # print(i, j)
            if board[i][j] == 'O':
                q = collections.deque([(i, j)])
                board[i][j] = 'o'
                while q:
                    tmp = q.pop()
                    for x, y in neighbor(*tmp):
                        if board[x][y] == 'O':
                            q.appendleft((x, y))
                            board[x][y] = 'o'
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'o' else 'X'



if __name__ == "__main__":
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s.solve(board)
    for row in board:
        print(row)
