from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = [mat[0][0]]

        for s in range(1, m + n - 1):
            if s & 1 == 1:
                # right to left
                for y in range(min(s, n - 1), -1, -1):
                    x = s - y
                    if x >= m:
                        break
                    # print(x, y)
                    ans.append(mat[x][y])
            else:
                # left to right
                for x in range(min(s, m - 1), -1, -1):
                    y = s - x
                    if y >= n:
                        break
                    # print(x, y)
                    ans.append(mat[x][y])

        return ans


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().findDiagonalOrder(mat))
