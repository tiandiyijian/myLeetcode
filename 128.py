from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        num_index = {num: i for i, num in enumerate(nums)}
        indices = set(range(0, len(nums)))
        parent = list(range(len(nums)))
        for i in range(len(nums)):
            index = num_index.get(nums[i]-1, None)
            # print(i, nums[i], index)
            if index is not None:
                parent[i] = index
                indices.discard(index)
            # else:
            #     indices.discard(i)
        ans = 0
        for i in indices:
            # p = i
            length = 1
            while i != parent[i]:
                i = parent[i]
                length += 1
            ans = max(ans, length)
        # print(parent, indices)
        return ans
        """
        num_set = set(nums)
        ans = 0
        for num in nums:
            if not num - 1 in num_set:
                cur = num
                while cur + 1 in num_set:
                    cur += 1
                ans = max(ans, cur - num + 1)
        return ans        

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    print(s.longestConsecutive(nums))
