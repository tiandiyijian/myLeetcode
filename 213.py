from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        c = 0
        d = nums[1]
        b = max(nums[1], nums[0])
        a = nums[0]
        for i in range(2, len(nums) - 1):
            a, b = b, max(nums[i] + a, b)
            c, d = d, max(nums[i] + c, d)
        c, d = d, max(nums[-1] + c, d)
        return max(b, d)


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2, 3, 2]))
