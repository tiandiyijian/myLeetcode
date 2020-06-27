from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while 0 < nums[i] <= N and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                print(i, nums)
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        return N + 1


if __name__ == "__main__":
    s = Solution()
    l = [3,4,3,1]
    print(s.firstMissingPositive(l))