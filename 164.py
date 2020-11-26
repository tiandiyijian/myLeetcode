from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_num = min(nums)
        max_num = max(nums)
        d = max(1, (max_num - min_num) // (len(nums) - 1))
        buckets_size = (max_num - min_num) // d + 1
        buckets = [[None] * 2 for _ in range(buckets_size)]
        for num in nums:
            idx = (num - min_num) // d
            if not buckets[idx][0]:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        ans = 0
        prev_max = None
        for i in range(buckets_size):
            if prev_max is None:
                prev_max = buckets[i][1]
                continue
            elif buckets[i][0] is None:
                continue
            else:
                ans = max(ans, buckets[i][0] - prev_max)
                prev_max = buckets[i][1]
        return ans

if __name__ == "__main__":
    s = Solution()
    l = [1,1,1,1,1,5,5,5,5,5]
    print(s.maximumGap(l))
