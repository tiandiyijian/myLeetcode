# class Solution:
#     def removeDuplicates(self, nums: list) -> int:
#         if len(nums) < 2:
#             return len(nums)
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)<2:
            return len(nums)
        subscript = 0
        for num in nums:
            if num != nums[subscript]:
                subscript += 1
                nums[subscript] = num
        return subscript + 1

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2,3,3,3,4]
    print(s.removeDuplicates(nums))
    print(nums)
        