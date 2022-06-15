from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        # k -= 1
        while l < r:
            mid = (l + r) >> 1
            cnt = 0
            i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            # for i in range(n):
            #     j = bisect_right(nums, mid + nums[i], i) - 1
            #     # print(1, i, j)
            #     cnt += j - i
            # lo, hi = i, n - 1
            # target = nums[i] + mid
            # while lo < hi:
            #     mmid = (lo+hi+1)>>1
            #     if nums[mmid] > target:
            #         hi = mmid - 1
            #     else:
            #         lo = mmid
            # print(i, lo)
            # cnt += lo - i
            # print(l, r, mid, cnt)
            if cnt > k:
                r = mid
            elif cnt < k:
                l = mid + 1
            else:
                r = mid
        return r

    def smallestDistancePair2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        def count(mid):
            cnt = 0
            i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) >> 1
            cnt = count(mid)
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        return r
    
nums = [62, 100, 4]
k = 2
# nums = [9,10,7,10,6,1,5,4,9,8]
# k = 18
# nums = [10,6,2,10,5,4,0,1,5,2,5,5,5,0,4,9,8,6,7,9,1,10,4,8,6,3,6,2,1,7,5,0,2,6,10,10,0,3,9,0,8,3,5,9,4,4,5,2,2,7]
# k = 444
print(Solution().smallestDistancePair(nums, k))
