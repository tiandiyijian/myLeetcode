class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [0] * len(nums)
        size = 0
        for ele in nums:
            l, r = 0, size
            while l != r: #找到dp中第一个不小于ele的元素
                mid = int((l + r) / 2)
                if dp[mid] < ele:
                    l = mid + 1
                else:
                    r = mid
                if r > size:
                    dp[r] = ele
            size = max(size, r+1)
        print(dp)
        return size

if __name__ == '__main__':
    a = Solution()
    nums = [2,3,8,11,7]
    print(a.lengthOfLIS(nums))