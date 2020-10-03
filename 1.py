from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in history:
                return [history[target - nums[i]], i]
            else:
                history[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    print()
