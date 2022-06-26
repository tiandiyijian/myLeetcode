from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)

        n = len(nums1)
        maxGain1 = maxGain2 = 0
        pre1 = pre2 = 0
        for i in range(n):
            cur1 = max(pre1, 0) + (nums2[i] - nums1[i])
            maxGain1 = max(maxGain1, cur1)
            pre1 = cur1

            cur2 = max(pre2, 0) + (nums1[i] - nums2[i])
            maxGain2 = max(maxGain2, cur2)
            pre2 = cur2

        ans = max(s1 + maxGain1, s2 + maxGain2)
        return ans

nums1 = [60,60,60]
nums2 = [10,90,10]
nums1 = [20,40,20,70,30]
nums2 = [50,20,50,40,20]
nums1 = [7,11,13]
nums2 = [1,1,1]
print(Solution().maximumsSplicedArray(nums1, nums2))