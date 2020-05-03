from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.sloved = False
        def valid(row, col, num):
            if num in board[row]:
                return False
            for i in range(9):
                if board[i][col] == num:
                    return False
            area_i, area_j = row // 3, col // 3
            for i in range(area_i * 3, area_i * 3 + 3):
                for j in range(area_j * 3, area_j * 3 + 3):
                    if board[i][j] == num:
                        return False
            return True

        def candidates(row, col):
            all_candidates = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for num in board[row]:
                if num != '.':
                    all_candidates.discard(num)
                    # print(num)
            for i in range(9):
                if board[i][col] != '.':
                    all_candidates.discard(board[i][col])
                    # print(board[i][col])
            area_i, area_j = row // 3, col // 3
            for i in range(area_i * 3, area_i * 3 + 3):
                for j in range(area_j * 3, area_j * 3 + 3):
                    if board[i][j] != '.':
                        all_candidates.discard(board[i][j])
                        # print(board[i][j])
            return all_candidates

        def dfs(row, col):
            if self.sloved:
                return
            next_row, next_col = row + (col + 1) // 9, (col + 1) % 9
            if row == 9:
                print(row, col)
                print('done')
                self.sloved = True
                # print(board)
                return
            if board[row][col] != '.' and not self.sloved:
                # print(row, col)
                dfs(next_row, next_col)
                return
            # tmp_num = board[row][col]
            # print(tmp_num)
            c = candidates(row, col)
            # print(c)
            if c:
                for num in candidates(row, col):
                    num = str(num)
                    # print(type(num))
                    # if valid(row, col, num) and not self.sloved:
                    if not self.sloved:
                        board[row][col] = num
                        dfs(next_row, next_col)
                        if not self.sloved:
                            board[row][col] = '.'
        dfs(0, 0)
        for i in board:
            print(i)


if __name__ == "__main__":
    s = Solution()
    b = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    b = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    for i in b:
        print(i)
    print('------')
    print(s.solveSudoku(b))
