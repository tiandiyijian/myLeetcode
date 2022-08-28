from typing import List


class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        n1, n2 = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(n1)
                n1 += 1
            else:
                ans.append(n2)
                n2 -= 1
        ans.append(n1)
        return ans
