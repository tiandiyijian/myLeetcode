import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        bucket = [None] * (len(nums) + 1)
        for num, freq in count.items():
            if not bucket[freq]:
                bucket[freq] = []
            bucket[freq].append(num)
        ans = []
        for nums in bucket[::-1]:
            if nums:
                for n in nums:
                    ans.append(n)
                    if len(ans) == k:
                        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([3, 0, 1, 0], 1))