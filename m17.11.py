from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.mp = None
    
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        if self.mp is None:
            mp = defaultdict(list)
            for i, word in enumerate(words):
                mp[word].append(i)
        
        l1 = mp[word1]
        l2 = mp[word2]
        ans = len(words)
        i1 = i2 = 0
        n1, n2 = len(l1), len(l2)
        
        while i1 < n1 and i2 < n2:
            ans = min(ans, abs(l1[i1]-l2[i2]))
            if i1 < n1 and l1[i1] < l2[i2]:
                i1 += 1
            else:
                i2 += 1
        return ans
        
        
        