from typing import List


class Solution_0:
    # 错在虽然子数组中不能有比right大的但是可以有多个比left小的元素
    # 所以应该重点关注比right大的
    # 如果要使用贡献法的话应该是先求得符合条件的元素左右比right大的索引
    # 然后每个元素的贡献是(i - l[i])*(r[i] - i)，不用考虑比left小的元素
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        ans = 0

        f = lambda n: (n + 1) * n // 2

        l = -1
        mid = -1
        for r in range(n):
            if not left <= nums[r] <= right:
                if mid > 0:
                    ans += f(mid - l - 1)
                    if nums[mid] < left:
                        ans += (
                            (mid - l - 1)
                            + (r - mid - 1)
                            + (mid - l - 1) * (r - mid - 1)
                        )
                l, mid = mid, r
        r = n
        ans += f(mid - l - 1) + f(r - mid - 1)
        if nums[mid] < left:
            ans += (mid - l) * (r - mid)
        return ans


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        ans = 0

        l = mid = -1
        for r in range(n):
            if nums[r] > right:
                l = mid = r
            if left <= nums[r] <= right:
                mid = r
            ans += mid - l

        return ans


nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
left = 32
right = 69
print(Solution().numSubarrayBoundedMax(nums, left, right))
