import collections
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ordered_nums = sorted(nums)
        num_to_idx = collections.defaultdict(list)
        for i, num in enumerate(nums):
            num_to_idx[num].append(i)
        count = 1
        for i in range(1, len(ordered_nums)):
            if ordered_nums[i] == ordered_nums[i-1]:
                count += 1
                continue
            for idx in num_to_idx[ordered_nums[i]]:
                ans[idx] = count
            count += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
