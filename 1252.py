from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_add = [0] * m
        col_cnt = [0] * n
        for x, y in indices:
            row_add[x] ^= 1
            col_cnt[y] ^= 1

        col_odd = sum(col_cnt)
        col_even = n - col_odd

        return sum(col_odd if x == 0 else col_even for x in row_add)
