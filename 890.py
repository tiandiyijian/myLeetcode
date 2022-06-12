from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        set_p = set(pattern)
        ans = []
        for word in words:
            if len(set(word)) != len(set_p):
                continue
            mp = {}
            mp_rev = {}
            for a, b in zip(pattern, word):
                if a not in mp and b not in mp_rev:
                    mp[a] = b
                    mp_rev[b] = a
                elif a in mp and b in mp_rev:
                    if mp[a] != b or mp_rev[b] != a:
                        break
                else:
                    break
            else:
                ans.append(word)
        return ans

words = ["abc","deq","mee","aqq","dkd","ccc"]
# words = ['dkd']
p="abb"
print(Solution().findAndReplacePattern(words, p))