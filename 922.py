from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        a, b = 0, 1
        s = len(A)
        while a < s and b < s:
            while a < s and A[a] & 1 == 0:
                a += 2
            while b < s and A[b] & 1 == 1:
                b += 2
            if a < s and b < s:
                A[a], A[b] = A[b], A[a]
        return A


if __name__ == "__main__":
    s = Solution()
    print()
