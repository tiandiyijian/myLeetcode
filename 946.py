from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        n = len(pushed)
        stk = []
        for v in popped:
            while not stk or stk[-1] != v:
                if i >= n:
                    return False
                stk.append(pushed[i])
                i += 1
            stk.pop()
        return True
