from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        r = 1
        ans = len(nums) + 1
        while l < len(nums):
            while sum(nums[l:r]) < s and r <= len(nums):
                r += 1
            if r > len(nums):
                return ans if ans < len(nums) + 1 else 0
            else:
                print(l, r)
                ans = min(ans, r - l)
            l += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    m = 7
    nums = [2,3,1,2,4,3]
    print(s.minSubArrayLen(m, nums))