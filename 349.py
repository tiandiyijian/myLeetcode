from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums2 = set(nums2)
        ans = set()
        for i in nums1:
            if i in nums2:
                ans.add(i)
        return list(ans)


if __name__ == "__main__":
    s = Solution()
    print()
