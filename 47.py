from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(depth, path):
            if depth == len(nums):
                ans.append(path)
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i - 1]):
                    continue
                # path.append(nums[i])
                used[i] = True
                dfs(depth + 1, path + [nums[i]])
                # path.pop()
                used[i] = False

        dfs(0, [])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
