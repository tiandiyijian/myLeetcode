from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {val:idx for idx, val in enumerate(nums1)}
        s = []
        ans = [0] * len(nums1)
        for val in nums2[::-1]:
            while s and s[-1] <= val:
                s.pop()
            bigger_num = s[-1] if s else -1
            if val in mp:
                ans[mp[val]] = bigger_num
            s.append(val)
        return ans