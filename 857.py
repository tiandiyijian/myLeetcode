import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        # 我想到了一组工人所需的最小金额只跟总质量以及最大的q/w有关
        # 但是没想到怎么同时维护这两个信息
        # 直接按照q/w排序后确保当前选中的工人可以直接从q/w比它小的工人中挑选q最小的k个
        # 而维护最小的k个明显可以用大顶堆
        pairs = sorted(list(zip(quality, wage)), key=lambda x: x[1] / x[0])
        totalq = 0
        h = []
        # 堆里面只保留k-1个
        for q, w in pairs[: k - 1]:
            totalq += q
            heapq.heappush(h, -q)

        ans = float('inf')
        for q, w in pairs[k - 1 :]:
            totalq += q
            ans = min(ans, totalq * w / q)
            totalq += heapq.heappushpop(h, -q)

        return ans
