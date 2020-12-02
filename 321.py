from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        maxSubsequence = [0] * k
        start, end = max(0, k - n), min(k, m)
        
        for i in range(start, end + 1):
            subsequence1 = self.getMaxSubsequence(nums1, i)
            subsequence2 = self.getMaxSubsequence(nums2, k - i)
            # print(subsequence1, subsequence2)
            curMaxSubsequence = self.merge(subsequence1, subsequence2)
            if self.compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0:
                maxSubsequence = curMaxSubsequence

        return maxSubsequence

    def getMaxSubsequence(self, nums: List[int], k: int) -> int:
        stack = [0] * k
        remain = len(nums) - k
        top = -1

        for num in nums:
            while top >= 0 and num > stack[top] and remain > 0:
                # 如果remain为0,就不再弹出元素,目的是为了保证最后stack中一定有k个元素
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1

        return stack

    def merge(self, subsequence1: List[int], subsequence2: List[int]) -> List[int]:
        m, n = len(subsequence1), len(subsequence2)

        if m == 0:
            return subsequence2
        if n == 0:
            return subsequence1

        i = j = idx = 0
        ans = [0] * (m + n)
        while i < m and j < n:
            if subsequence1[i] > subsequence2[j]:
                ans[idx] = subsequence1[i]
                i += 1
            elif subsequence1[i] < subsequence2[j]:
                ans[idx] = subsequence2[j]
                j += 1
            else:
                # 如果这两个数相等就要考虑这两个数后面的数
                if self.compare(subsequence1, i, subsequence2, j) > 0:
                    ans[idx] = subsequence1[i]
                    i += 1
                else:
                    ans[idx] = subsequence2[j]
                    j += 1
            idx += 1
            
        ans[idx:] = subsequence2[j:] if i == m else subsequence1[i:]
        return ans

    def compare(self, subsequence1: List[int], index1: int, subsequence2: List[int], index2: int) -> int:
        m, n = len(subsequence1), len(subsequence2)
        while index1 < m and index2 < n:
            diff = subsequence1[index1] - subsequence2[index2]
            if diff != 0:
                return diff
            index1 += 1
            index2 += 1
        return (m - index1) - (n - index2)

if __name__ == "__main__":
    s = Solution()
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    print(s.maxNumber(nums1, nums2, 5))
