class Solution:
    def search(self, nums: list, target: int) -> int:
        size = len(nums)
        i, j = 0, size - 1
        while j >= i:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[i]:
                if nums[mid] > target >= nums[i]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([3,1], 1))            