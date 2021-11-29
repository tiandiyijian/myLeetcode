from typing import List
import heapq

class Score:
    def __init__(self, i, j, a, b):
        self.i = i
        self.j = j
        self.a = a
        self.b = b
    
    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = [Score(0, j, arr[0], arr[j]) for j in range(1, n)]
        heapq.heapify(q)
        for _ in range(k-1):
            S = heapq.heappop(q)
            if S.i + 1 < S.j:
                heapq.heappush(q, Score(S.i+1, S.j, arr[S.i+1], arr[S.j]))
        return [q[0].a, q[0].b]