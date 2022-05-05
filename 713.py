from typing import List


class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = 0
        n = len(nums)

        cur = 1
        r = 0
        for l in range(n):
            if l > 0 and l <= r:
                cur //= nums[l - 1]
            if cur > k:
                continue
            r = max(r, l)
            while r < n and (tmp := cur * nums[r]) < k:
                cur = tmp
                r += 1
                ans += r - l

            print(l, r, cur, ans)

        return ans


l = [10, 5, 2, 6]
k = 100
print(Solution().numSubarrayProductLessThanK(l, k))
