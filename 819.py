from collections import Counter
from typing import List


class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnter = Counter(
            paragraph.replace("!", " ").replace("?", " ").replace(
                "'",
                " ").replace(",",
                             " ").replace(";",
                                          " ").replace(".",
                                                       " ").lower().split())
        banned = set(banned)
        ans = None
        maxCnt = 0
        for k, v in cnter.items():
            if v > maxCnt and k not in banned:
                ans = k
                maxCnt = v
            # print(k, v, maxCnt)
        # print(cnter)
        return ans