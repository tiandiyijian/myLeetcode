from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                # break
                slow = 0
                while nums[slow] != nums[fast]:
                    slow = nums[slow]
                    fast = nums[fast]
                return nums[slow]


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 2, 4, 3]))
