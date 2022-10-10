from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a = 0
        b = 1

        for i in range(1, n):
            pa, pb = a, b
            a = b = n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                a = pa
                b = pb + 1
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                a = min(a, pb)
                b = min(b, pa + 1)
            # print(a, b)
        return min(a, b)
