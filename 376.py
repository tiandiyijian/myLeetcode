from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (size := len(nums)) < 2:
            return size
        pre_diff = nums[1] - nums[0]
        ans = 2 if pre_diff else 1
        for i in range(2, size):
            diff = nums[i] - nums[i-1]
            if (pre_diff >= 0 and diff < 0) or (pre_diff <= 0 and diff > 0):
                ans += 1
                pre_diff = diff
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.wiggleMaxLength([1, 3, 2, 4, 5, 5]))
