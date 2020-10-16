from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        ans = [0] * len(A)
        for i in range(len(A) - 1, -1, -1):
            if abs(A[l]) >= abs(A[r]):
                ans[i] = A[l]**2
                l += 1
            else:
                ans[i] = A[r]**2
                r -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
