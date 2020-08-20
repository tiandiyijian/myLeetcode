from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        m, n = len(board), len(board[0])

        def dfs(x, y):
            count = 0
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'M':
                    count += 1
            if count > 0:
                board[x][y] = str(count)
                return
            board[x][y] = 'B'
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
                if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                    dfs(i, j)

        dfs(x, y)
        return board


if __name__ == "__main__":
    s = Solution()
    board = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    print(s.updateBoard(board, click))
