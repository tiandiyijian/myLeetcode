from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, e in enumerate(nums):
            if i == e:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findMagicIndex([1, 1, 1]))
