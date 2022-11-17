from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        char_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_indices[c].append(i)

        ans = 0
        for w in words:
            if len(w) > n:
                continue

            i = -1
            for c in w:
                cur_indices = char_indices[c]
                j = bisect_right(cur_indices, i)
                if j == len(cur_indices):
                    break
                i = cur_indices[j]
            else:
                ans += 1

        return ans


s = "abcde"
words = ["a", "bb", "acd", "ace"]
print(Solution().numMatchingSubseq(s, words))
