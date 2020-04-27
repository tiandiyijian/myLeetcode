class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False
