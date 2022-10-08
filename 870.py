from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)

        indices1 = list(range(n))
        indices2 = list(range(n))
        indices1.sort(key=lambda i: nums1[i])
        indices2.sort(key=lambda i: nums2[i])
        # print(indices1, indices2)

        ans = [-1] * n
        back = n - 1
        i1 = i2 = 0
        while i2 < n:
            while i1 < n and nums1[indices1[i1]] <= nums2[indices2[i2]]:
                # print(indices2[back], indices1[i1])
                ans[indices2[back]] = nums1[indices1[i1]]
                back -= 1
                i1 += 1
            if i1 < n:
                ans[indices2[i2]] = nums1[indices1[i1]]
                i1 += 1
            else:
                return ans

            i2 += 1

        return ans
