from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        start = end = 0
        ans = 0
        while start < len(A) - 2:
            if A[start] >= A[start + 1]:
                start += 1
            else:
                peek = start + 1
                while peek < len(A) - 1 and A[peek] < A[peek + 1]:
                    peek += 1
                if peek == len(A) - 1:
                    return ans
                end = peek + 1
                if A[end] == A[peek]:
                    start = end
                    continue
                while end < len(A) - 1 and A[end] > A[end + 1]:
                    end += 1
                print(start, peek, end)
                ans = max(ans, end - start + 1)
                start = end
        return ans


if __name__ == "__main__":
    s = Solution()
    # A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    A = [0, 2, 2]
    print(s.longestMountain(A))
