from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        def liveCellsAround(x, y):
            count = 0
            for i, j in offsets:
                p, q = x + i, y + j
                if 0 <= p < m and 0 <= q < n and (board[p][q] == 1 or board[p][q] == -1):
                    count += 1
            return count
        for i in range(m):
            for j in range(n):
                liveCells = liveCellsAround(i, j)
                if board[i][j] == 1:
                    if liveCells < 2 or liveCells > 3:
                        board[i][j] = -1 # 现在活将来死
                elif board[i][j] == 0:
                    if liveCells == 3:
                        board[i][j] = -2 # 现在死将来活
        print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == -2:
                    board[i][j] = 1
        return board

if __name__ == "__main__":
    s = Solution()
    l = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    l = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    l = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    print(s.gameOfLife(l))
