import collections
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), len(nums[0])
        indices = collections.defaultdict(list)
        low, high = float('inf'), float('-inf')
        for i in range(m):
            low = min(low, nums[i][0])
            high = max(high, nums[i][-1])
            for n in nums[i]:
                indices[n].append(i)
        left = right = low
        ans_l, ans_r = low, high
        counter = [0] * m
        inside = 0
        while right <= high:
            if right in indices:
                for idx in indices[right]:
                    counter[idx] += 1
                    if counter[idx] == 1:
                        inside += 1
            # print(left, right, counter)
            while inside == m:
                if right - left < ans_r - ans_l:
                    ans_l, ans_r = left, right
                if left in indices:
                    for idx in indices[left]:
                        counter[idx] -= 1
                        if counter[idx] == 0:
                            inside -= 1
                left += 1
            right += 1

        return [ans_l, ans_r]


if __name__ == "__main__":
    s = Solution()
    nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(s.smallestRange(nums))
