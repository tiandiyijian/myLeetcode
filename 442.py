from typing import List


class Solution:
    # 像这种要求使用常数额外空间的问题一般都是想办法借助输入的列表本身解决问题
    # 常见的方法就是换位置和利用符号做标记
    def findDuplicates1(self, nums: List[int]) -> List[int]:
        ans = set()
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    # ans.append(nums[i])
                    ans.add(nums[i])
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            #     print(i, nums)
            # print(i, ans)
        return list(ans)

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i] - 1]
        return [x for i, x in enumerate(nums) if i + 1 != x]

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] > 0:
                nums[x - 1] = -nums[x - 1]
            else:
                ans.append(x)
        return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDuplicates(nums))
