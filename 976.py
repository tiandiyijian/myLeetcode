from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        for i in range(len(A) - 1, 1, -1):
            if A[i-1] + A[i-2] > A[i]:
                return A[i-1] + A[i-2] + A[i]
        return 0


if __name__ == "__main__":
    s = Solution()
    print()