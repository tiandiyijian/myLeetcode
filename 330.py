from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_num = 1
        ans = 0
        size = len(nums)
        idx = 0
        while max_num <= n:
            if idx < size and nums[idx] <= max_num:
                max_num += nums[idx]
                idx += 1
            else:
                print(max_num)
                max_num <<= 1
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.minPatches([1, 3], 6))
