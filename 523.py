from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_dict = {0: -1}
        sum_mod = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sum_mod[i + 1] = (sum_mod[i] + nums[i]
                              ) % k if k != 0 else sum_mod[i] + nums[i]
            if sum_mod[i + 1] in mod_dict:
                if i - mod_dict[sum_mod[i+1]] > 1:
                    return True
            else:
                mod_dict[sum_mod[i + 1]] = i
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkSubarraySum([0, 0], 0))
