from typing import List

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x):
            cnt, tmp_sum = 1, 0
            for n in nums:
                if n + tmp_sum > x:
                    tmp_sum = n
                    cnt += 1
                    if m < cnt:
                        return False
                else:
                    tmp_sum += n
            return m >= cnt
        
        lo, hi = max(nums), sum(nums)
        # print(lo, hi)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
            # print(lo, hi)
        # print(lo, hi)
        return lo


if __name__ == "__main__":
    s = Solution()
    l = [7,2,5,10,8]
    m = 2
    print(s.splitArray(l, m))