from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        current_min = 1
        current_max = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            current_max = max(current_max * nums[i], nums[i])
            current_min = min(current_min * nums[i], nums[i])
            ans = max(ans, current_max)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -1, 4]))
