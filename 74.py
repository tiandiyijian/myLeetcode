from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        first_col = [matrix[i][0] for i in range(m)]
        i = bisect.bisect(first_col, target) - 1
        if i > 0 and first_col[i] == target:
            return True
        j = bisect.bisect_left(matrix[i], target)
        return j < n and matrix[i][j] == target
