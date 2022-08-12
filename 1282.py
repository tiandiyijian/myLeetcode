from functools import reduce
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        groups = [[] for _ in range(n + 1)]

        for i, size in enumerate(groupSizes):
            if not groups[size]:
                groups[size].append([i])
            else:
                if len(groups[size][-1]) == size:
                    groups[size].append([i])
                else:
                    groups[size][-1].append(i)

        return reduce(lambda x, y: x + y, groups, [])
