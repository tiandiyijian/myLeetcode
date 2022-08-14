from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        inDeg = [0] * n
        ans = 0
        ansInDeg = 0

        for i, tar in enumerate(edges):
            inDeg[tar] += i
            if inDeg[tar] > ansInDeg:
                ans = tar
                ansInDeg = inDeg[tar]
            elif inDeg[tar] == ansInDeg:
                if tar < ans:
                    ans = tar
                    ansInDeg = inDeg[tar]
        return ans
