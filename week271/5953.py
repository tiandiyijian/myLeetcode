from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        nums.append(float('inf'))
        stack = [-1]
        for i in range(n+1):
            while nums[i] > nums[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                ans += nums[j] * (j - k) * (i - j)
            stack.append(i)
        # print(ans)
        nums[-1] = float('-inf')
        stack = [-1]
        for i in range(n+1):
            while nums[i] < nums[stack[-1]]:
                j = stack.pop()
                k = stack[-1]
                ans -= nums[j] * (j - k) * (i - j)
            stack.append(i)
        return ans


nums = [1, 1, 1]
print(Solution().subArrayRanges(nums))
