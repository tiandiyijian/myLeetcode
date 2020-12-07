from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        ans = 0
        for j in range(n):
            ones = 0
            for i in range(m):
                if (A[i][0] == 0 and A[i][j] == 0) or (A[i][0] == 1 and A[i][j] == 1):
                    ones += 1
            ans += max(ones, m - ones) * pow(2, n - j - 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
