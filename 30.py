from collections import Counter, defaultdict
from typing import List

from black import diff


class Solution:
    def findSubstring0(self, s: str, words: List[str]) -> List[int]:
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

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, p, w = len(s), len(words[0]), len(words)
        ans = []

        for start in range(p):
            # print(f'{start=}')
            if start + w * p > n:
                break
            diff = Counter(words)
            # print(diff)
            for i in range(start, start + w * p, p):
                x = s[i : i + p]
                diff[x] -= 1
                if x in diff and diff[x] == 0:
                    del diff[x]
            if len(diff) == 0:
                ans.append(start)
            # print(diff, ans)
            for i in range(start + p, n - w * p + 1, p):
                diff[s[i - p : i]] += 1
                if diff[s[i - p : i]] == 0:
                    del diff[s[i - p : i]]
                diff[s[i + (w - 1) * p : i + w * p]] -= 1
                if diff[s[i + (w - 1) * p : i + w * p]] == 0:
                    del diff[s[i + (w - 1) * p : i + w * p]]
                # print(i, diff)
                if len(diff) == 0:
                    ans.append(i)

        return ans


s = "barfoobarfoobar"
ws = ["foo", "bar"]
s = "barfoofoobarthefoobarman"
ws = ["bar", "foo", "the"]
print(Solution().findSubstring(s, ws))
