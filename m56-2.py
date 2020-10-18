from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = [0] * 32
        for n in nums:
            i = 0
            while n:
                bit[i] += n & 1
                n >>= 1
                i += 1
        ans = 0
        for i in range(32):
            if bit[i] % 3 == 1:
                ans ^= 1 << i
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([3,4,3,3]))
