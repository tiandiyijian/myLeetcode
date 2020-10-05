from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        i = 0
        while i < length - 3:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                i += 1
                continue
            j = i + 1
            while j < length - 2:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    j += 1
                    continue
                tmp_sum = nums[i] + nums[j]
                tar = target - tmp_sum
                l = j + 1
                r = length - 1
                while l < r:
                    if nums[l] + nums[r] == tar:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l + 1 < r and nums[l + 1] == nums[l]:
                            l += 1
                        l += 1
                    elif nums[l] + nums[r] > tar:
                        r -= 1
                    else:
                        l += 1
                j += 1
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
