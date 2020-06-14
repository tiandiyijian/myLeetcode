from typing import List
import bisect


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        pre_sum = [0] * (n + 1)
        # pre_sum[0] = arr[0]
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + arr[i-1]
        l, r = 0, arr[n-1]
        # print(l, r)
        point = 0
        while l <= r:
            mid = (l + r) // 2
            
            idx = bisect.bisect_left(arr, mid)
            tmp = pre_sum[idx] + (n-idx) * mid
            # print(l, r, mid, idx, tmp)
            if tmp > target:
                r = mid - 1
            else:
                l = mid + 1
                point = mid

        
        l_sum = sum(x if x < point else point for x in arr)
        r_sum = sum(x if x < point+1 else point+1 for x in arr)
        # print(point, l_sum, r_sum)
        return point if abs(l_sum-target) <= abs(r_sum-target) else point + 1


if __name__ == "__main__":
    s = Solution()
    l = [2,3,5]
    t = 10
    print(s.findBestValue(l, t))
