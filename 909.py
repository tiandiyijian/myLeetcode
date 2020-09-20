import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        def get_tar(x):
            nonlocal N
            row = ((N - 1) - (x - 1) // N)
            col = (x - 1) % N
            if (x - 1) // N & 1:
                col = (N - 1) - col
            # print(x, row, col)
            return board[row][col]
        
        destination = N * N
        visited = set()
        q = collections.deque()
        q.appendleft(1)
        count = 0
        while q:
            tmp_len = len(q)
            for _ in range(tmp_len):
                x = q.pop()
                visited.add(x)
                if x == destination:
                    return count
                for nxt in range(min(x + 6, destination), x, -1):
                    tar = get_tar(nxt)
                    if tar != -1 and not tar in visited:
                        q.appendleft(tar)
                for nxt in range(min(x + 6, destination), x, -1):
                    tar = get_tar(nxt)
                    if tar == -1 and not nxt in visited:
                        q.appendleft(nxt)
                        break
            count += 1
            # print(q, count)
        return -1
        

if __name__ == "__main__":
    s = Solution()
    board = [[1,1,-1],[1,1,1],[-1,1,1]]
    print(s.snakesAndLadders(board))