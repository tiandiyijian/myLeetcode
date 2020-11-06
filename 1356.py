from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_of_ones(num):
            count = 0
            while num:
                if num & 1:
                    count += 1
                num >>= 1
            return count

        buckets = [[] for _ in range(15)]

        for num in arr:
            buckets[count_of_ones(num)].append(num)

        ans = []
        for bucket in buckets:
            if bucket:
                bucket.sort()
            ans.extend(bucket)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
