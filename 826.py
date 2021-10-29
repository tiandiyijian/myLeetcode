import bisect
import collections
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        best_work = collections.defaultdict(int)
        for d, p in zip(difficulty, profit):
            best_work[d] = max(p, best_work[d])

        difficulty.sort()
        for i in range(1, n):
            best_work[difficulty[i]] = max(best_work[difficulty[i-1]], best_work[difficulty[i]])
        # print(best_work)
        # print(difficulty)
        ans = 0
        idx = 0
        pre_idx = 0
        for w in sorted(worker):
            idx = bisect.bisect_left(difficulty, w, pre_idx)
            if idx == n or difficulty[idx] > w:
                idx -= 1
            if idx < 0:
                continue
            pre_idx = idx
            # print(w, idx, difficulty[idx])
            ans += best_work[difficulty[idx]]
        return ans

if __name__ == '__main__':
    s = Solution()
    difficulty = [68,35,52,47,86]
    profit = [67,17,1,81,3]
    worker = [92,10,85,84,82]
    print(s.maxProfitAssignment(difficulty, profit, worker))