from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []

        left = 0
        while left < n:
            right = left + 1
            while right < n and nums[right] <= nums[right - 1] + 1:
                right += 1
            ans.append(
                f'{nums[left]}->{nums[right-1]}' if right - 1 > left else f'{nums[left]}')
            left = right

        return ans


if __name__ == "__main__":
    s = Solution()
    print()
