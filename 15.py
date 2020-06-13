from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            else:
                tmp = -nums[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] > tmp:
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                    elif nums[l] + nums[r] < tmp:
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
                    else:
                        ans.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        r -= 1
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        l += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    l = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(l))
