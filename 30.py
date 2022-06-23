from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        p = len(words[0])
        cnter = defaultdict(int)
        for word in words:
            cnter[word] += 1

        ans = []
        n = len(s)
        i = 0
        while i <= n - p:
            if s[i : i + p] in cnter:
                choose = defaultdict(int)
                choose[s[i : i + p]] = 1
                j = i + p
                while j <= n - p:
                    if (x := s[j : j + p]) in cnter:
                        if choose[x] == cnter[x]:
                            break
                        choose[x] += 1
                        j += p
                    else:
                        break
                for k, v in cnter.items():
                    if v != choose[k]:
                        break
                else:
                    ans.append(i)
                i += 1
            else:
                i += 1

        return ans

s = "barfoobarfoobar"
ws  = ["foo","bar"]
print(Solution().findSubstring(s, ws))
        