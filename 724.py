from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # isum = nums[:]
        # n = len(nums)
        # for i in range(1, n):
        #     isum[i] += isum[i-1]
        # # print(isum)
        # for i in range(n):
        #     if isum[i] - nums[i] == isum[-1] - isum[i]:
        #         return i
        # return -1
        # 使用O(1)的空间即可，没必要用整个数组存前缀和
        total = sum(nums)
        pre_sum = 0
        for i in range(len(nums)):
            if pre_sum == total - nums[i] - pre_sum:
                return i
            pre_sum += nums[i]
        return -1

if __name__ == "__main__":
    s = Solution()
    print()