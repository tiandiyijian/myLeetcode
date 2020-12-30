import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # big_heap = list(map(lambda x: -x, stones))
        big_heap = [-x for x in stones]
        heapq.heapify(big_heap)
        while len(big_heap) > 1:
            a, b = heapq.heappop(big_heap), heapq.heappop(big_heap)
            left = a - b
            if left < 0:
                heapq.heappush(big_heap, left)
        return -big_heap[0] if big_heap else 0


if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight([2, 7, 4, 1, 8, 1]))
