from typing import List

class Solution:
      def numRookCaptures(self, board: List[List[str]]) -> int:
            for i in range(64):
               r = i // 8
               c = i % 8
               if board[r][c] == 'R':
                  break         
            ans = 0
            # print(r,c)
            if r > 0:
               for i in range(r-1, -1, -1):
                  if board[i][c] == '.':
                     continue
                  elif board[i][c] == 'B':
                     break
                  elif board[i][c] == 'p':
                     ans += 1
                     break
            if r < 7:
               for i in range(r+1, 8):
                  if board[i][c] == '.':
                     continue
                  elif board[i][c] == 'B':
                     break
                  elif board[i][c] == 'p':
                     ans += 1
                     break
            if c > 0:
               for j in range(c-1, -1, -1):
                  if board[r][j] == '.':
                     continue
                  elif board[r][j] == 'B':
                     break
                  elif board[r][j] == 'p':
                     ans += 1
                     break
            if c < 8:
               for j in range(c+1, 8):
                  if board[r][j] == '.':
                     continue
                  elif board[r][j] == 'B':
                     break
                  elif board[r][j] == 'p':
                     ans += 1
                     break
            return ans

if __name__ == "__main__":
   s = Solution()
   b=[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
   print(s.numRookCaptures(b))