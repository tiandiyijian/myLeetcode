from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt, freq = Counter(), Counter()
        ans = 0
        maxFreq = 0

        for i, num in enumerate(nums):
            if cnt[num] in freq:
                freq[cnt[num]] -= 1

            cnt[num] += 1
            freq[cnt[num]] += 1
            if cnt[num] > maxFreq:
                maxFreq = cnt[num]
            # print(cnt, freq, maxFreq)
            if maxFreq == 1 or (
                freq[maxFreq] == 1 and freq[maxFreq-1] *
                    (maxFreq-1) + maxFreq == i + 1
            ) or (
                freq[maxFreq] * maxFreq + 1 == i + 1
            ):
                ans = i + 1

        return ans
