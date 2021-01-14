from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = len(A)
        val = 0
        ans = [False] * n

        for i in range(n):
            val = ((val << 1) + A[i]) % 5
            # print(val)
            if val % 5 == 0:
                ans[i] = True

        return ans


if __name__ == "__main__":
    s = Solution()
    print()
