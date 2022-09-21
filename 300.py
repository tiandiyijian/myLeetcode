from typing import List


class Solution:
    def lengthOfLIS0(self, nums) -> int:
        dp = [0] * len(nums)
        size = 0
        for ele in nums:
            l, r = 0, size
            while l != r:  # 找到dp中第一个不小于ele的元素
                mid = int((l + r) / 2)
                if dp[mid] < ele:
                    l = mid + 1
                else:
                    r = mid
                if r > size:
                    dp[r] = ele
            size = max(size, r + 1)
        print(dp)
        return size

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 1
        d = [float('-inf'), nums[0]]

        for i in range(1, n):
            if nums[i] > d[maxLen]:
                d.append(nums[i])
                maxLen += 1
                continue

            l = 0
            r = maxLen
            # 找到d中第一个不小于nums[i]的元素
            # 可以把它替换成nums[i]
            # 因为从贪心的角度来讲希望上升序列的末位越小越好
            while l < r:
                mid = (l + r) >> 1
                if d[mid] >= nums[i]:
                    r = mid
                else:
                    l = mid + 1
            d[l] = nums[i]

        return maxLen


if __name__ == '__main__':
    a = Solution()
    nums = [2, 3, 8, 11, 7]
    print(a.lengthOfLIS(nums))
