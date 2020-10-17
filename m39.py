from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for n in nums:
            if count == 0:
                ans = n
                count += 1
            elif ans != n:
                count -= 1
            else:
                count += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
