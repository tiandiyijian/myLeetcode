from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowCnt = [0] * m
        colCnt = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowCnt[i] += 1
                    colCnt[j] += 1

        return sum(
            mat[i][j] == 1
            for i in range(m)
            if rowCnt[i] == 1
            for j in range(n)
            if colCnt[j] == 1
        )
