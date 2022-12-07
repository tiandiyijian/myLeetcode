from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, s1 = len(nums1), sum(nums1)
        n2, s2 = len(nums2), sum(nums2)

        if s1 == s2:
            return 0

        if 6 * n1 < n2 or 6 * n2 < n1:
            return -1

        if s1 < s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        diff = s1 - s2
        to_decrease = Counter(nums1)
        to_increase = Counter(nums2)
        # print(diff, to_decrease, to_increase)

        ans = 0
        for a in range(1, 6):
            if to_increase[a] > 0 and diff > 0:
                cnt = min(to_increase[a], ceil(diff / (6 - a)))
                diff -= cnt * (6 - a)
                ans += cnt
                # print('a', diff, cnt, a)
            b = 7 - a
            if to_decrease[b] > 0 and diff > 0:
                cnt = min(to_decrease[b], ceil(diff / (b - 1)))
                diff -= cnt * (b - 1)
                ans += cnt
                # print('b', diff, cnt, b)
        return ans
