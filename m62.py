from typing import List


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        idx = 0
        length = n
        for _ in range(n-1):
            idx = (idx + m - 1) % length
            nums.pop(idx)
            length -= 1
        return nums[0]

    def lastRemaining1(self, n: int, m: int) -> int:
        ans = 0
        for length in range(2, n+1):
            ans = (ans + m) % length
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining1(10, 17))
