from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] > A[1]:
            return False
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i += 1
        if i == len(A):
            return False
        while i < len(A):
            if A[i] < A[i-1]:
                i += 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validMountainArray([1,2,3,3,4,2]))
