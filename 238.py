class Solution:
    def productExceptSelf(self, nums: list):
        # print(nums)
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = nums[i-1] * ans[i - 1]
        right = nums[-1]
        # print(ans)
        for i in range(len(nums) - 2, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))         