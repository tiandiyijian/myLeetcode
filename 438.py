from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = Counter(p)
        n = len(s)
        ans = []
        l = 0
        tmp_counter = defaultdict(int)
        for r in range(n):
            if s[r] not in c:
                l = r + 1
                tmp_counter = defaultdict(int)
                l = r + 1
            else:
                tmp_counter[s[r]] += 1
                if tmp_counter[s[r]] > c[s[r]]:
                    while s[l] != s[r]:
                        tmp_counter[s[l]] -= 1
                        l += 1
                    tmp_counter[s[l]] -= 1
                    l += 1
                elif r - l + 1 == len(p) and all(c[k] == tmp_counter[k] for k in c):
                    ans.append(l)
                    tmp_counter[s[l]] -= 1
                    l += 1
        return ans
