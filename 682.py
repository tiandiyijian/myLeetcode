from typing import List
from collections import deque


class Solution:

    def calPoints(self, ops: List[str]) -> int:
        s1 = deque([])
        for c in ops:
            if c == '+':
                s1.append(s1[-1] + s1[-2])
            elif c == 'C':
                s1.pop()
            elif c == 'D':
                s1.append(s1[-1] << 1)
            else:
                s1.append(int(c))
            # print(s1)
        return sum(s1)