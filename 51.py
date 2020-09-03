from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        diagonals1 = set()
        diagonals2 = set()

        def check(row, col):
            return not(col in cols or col - row in diagonals1 or col + row in diagonals2)

        def dfs(row, tmp):
            if row == n:
                ans.append([''.join(row) for row in tmp])
            else:
                for col in range(n):
                    if check(row, col):
                        tmp[row][col] = 'Q'
                        cols.add(col)
                        diagonals1.add(col - row)
                        diagonals2.add(col + row)
                        dfs(row + 1, tmp)
                        tmp[row][col] = '.'
                        cols.discard(col)
                        diagonals1.discard(col - row)
                        diagonals2.discard(col + row)

        tmp = [['.'] * n for _ in range(n)]
        dfs(0, tmp)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))