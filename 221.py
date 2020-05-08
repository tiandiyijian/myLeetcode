from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0 
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        maxSide = 0
        for i in range(rows):
            dp[i][0] = int(matrix[i][0])
            maxSide = max(maxSide, dp[i][0])
        for i in range(cols):
            dp[0][i] = int(matrix[0][i])
            maxSide = max(maxSide, dp[0][i])
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide ** 2


if __name__ == "__main__":
    s = Solution()
    print()