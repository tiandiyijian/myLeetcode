from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] >= 0:
            if k & 1 == 0:
                return sum(nums)
            else:
                return sum(nums) - (nums[0] << 1)
        n = len(nums)
        if nums[-1] <= 0:
            if k <= n:
                return -sum(nums[:k]) + sum(nums[k:])
            else:
                k -= n
                if k & 1 == 0:
                    return -sum(nums)
                else:
                    return -sum(nums) + (nums[-1] << 1)
        negatives = []
        for i in range(min(n, k)):
            if nums[i] < 0:
                negatives.append(-nums[i])
                k -= 1
            else:
                break
        print(negatives, k, i)
        if k == 0:
            return sum(negatives) + sum(nums[i+1:])
        else:
            nums = negatives + nums[i:]
            return self.largestSumAfterKNegations(nums, k)


nums = [5, 6, 9, -3, 3]
k = 2
print(Solution().largestSumAfterKNegations(nums, k))
