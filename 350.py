from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1
        ans = []
        idx = 0
        for i in range(l2):
            while idx < l1 and nums2[i] > nums1[idx]:
                idx += 1
            if idx == l1:
                return ans
            if nums2[i] < nums1[idx]:
                continue
            elif nums2[i] == nums1[idx]:
                idx += 1
                ans.append(nums2[i])
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 2]))
