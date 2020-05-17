from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        ans = []
        edges = collections.defaultdict(list)
        for edge in prerequisites:
            edges[edge[1]].append(edge[0])
            indeg[edge[0]] += 1
        q = collections.deque(
            [idx for idx, val in enumerate(indeg) if val == 0])
        while q:
            node = q.pop()
            ans.append(node)
            for out in edges[node]:
                indeg[out] -= 1
                if indeg[out] == 0:
                    q.appendleft(out)
        return ans if len(ans) == numCourses else []


if __name__ == "__main__":
    s = Solution()
    print()
