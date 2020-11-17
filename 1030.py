from collections import deque
from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        q = deque([(r0, c0)])
        visited = {(r0, c0)}
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            tmp_len = len(q)
            for _ in range(tmp_len):
                x, y = q.pop()
                for [dx, dy] in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in visited:
                        q.appendleft((nx, ny))
                        visited.add((nx, ny))
                        ans.append([nx, ny])
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
