from typing import List
from collections import Counter, defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        # cnt = collections.defaultdict(int)
        # for num in hand:
        #     cnt[num] += 1
        cnt = Counter(hand)
        nums = list(set(hand))
        nums.sort()
        for i in nums:
            if cnt[i] == 0:
                continue
            while cnt[i] > 0:
                for j in range(i, i+groupSize):
                    if cnt[j] == 0:
                        return False
                    cnt[j] -= 1
        return True
