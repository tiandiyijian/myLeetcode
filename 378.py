from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


if __name__ == "__main__":
    s = Solution()
    m = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(s.kthSmallest(m, 8))
