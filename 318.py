from collections import defaultdict
from typing import List
from functools import reduce



class Solution:
    def maxProduct(self, words: List[str]) -> int:
        c_to_int = {}
        n = 1
        for i in range(ord('a'), ord('z')+1):
            c_to_int[chr(i)] = n
            n <<= 1
        # print(c_to_int)
        # words.sort(key=len, reverse=True)
        ints = [reduce(lambda x, y: x | y, (c_to_int[c] for c in word)) if word else 0 for word in words]
        # print(ints)
        ans = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if ints[i] & ints[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
    
    def maxProduct1(self, words: List[str]) -> int:
        m = defaultdict(int)
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            m[mask] = max(m[mask], len(word))
        # print(m)
        ans = 0
        for x in m:
            for y in m:
                if x & y == 0:
                    ans = max(ans, m[x] * m[y])
        return ans

if __name__ == "__main__":
    s = Solution()
    l = ['a', 'aa', 'cb']
    print(s.maxProduct1(l))