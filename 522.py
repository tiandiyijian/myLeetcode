from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n = len(strs)
        ans = 0
        for i in range(n):
            s1 = strs[i]
            n1 = len(s1)
            for j in range(n):
                if j == i:
                    continue
                s2 = strs[j]
                n2 = len(s2)
                if len(s1) > len(s2):
                    continue
                p = q = 0
                while p < n1 and q < n2:
                    if s1[p] == s2[q]:
                        p += 1
                        q += 1
                    else:
                        q += 1
                if p == n1:
                    break
            else:
                ans = max(ans, n1)
        return ans
