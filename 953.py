from itertools import pairwise
from typing import List

class Solution:
    def isAlienSorted1(self, words: List[str], order: str) -> bool:
        order = {c:i for i, c in enumerate(order)}
        def less(a, b):
            for x, y in zip(a, b):
                if order[x] < order[y]:
                    return True
                elif order[x] > order[y]:
                    return False
            
            if len(a) <= len(b):
                return True
            return False

        for i in range(1, len(words)):
            if not less(words[i-1], words[i]):
                return False
        
        return True
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {c: i for i, c in enumerate(order)}
        print(list(pairwise([index[c] for c in word] for word in words)))
        return all(s <= t for s, t in pairwise([index[c] for c in word] for word in words))


words = ["hello","leetcode", "tian"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(Solution().isAlienSorted(words, order))