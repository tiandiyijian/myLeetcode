from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)

        def dfs(idx, last, seq):
            if idx == length:
                if len(seq) > 1:
                    ans.append(seq)
                return

            if nums[idx] == last:  # 必选选当前的，否则会出现重复的
                dfs(idx + 1, nums[idx], seq + [nums[idx]])
            elif nums[idx] > last:  # 可以选，也可以不选
                dfs(idx + 1, last, seq)
                dfs(idx + 1, nums[idx], seq + [nums[idx]])
            else:  # nums[idx] < last，不能选
                dfs(idx + 1, last, seq)

        dfs(0, -101, [])
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    print(s.findSubsequences(nums))
