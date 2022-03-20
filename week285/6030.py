from typing import List


from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        l = 0
        r = 0
        max_len = 1
        i = 0
        n = len(s)
        left = list(range(n))
        right = list(range(n))
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            if j - i > max_len:
                max_len = j - i
                l, r = i, j-1
            left[i:j] = [i] * (j-i)
            right[i:j] = [j-1] * (j-i)
        
        k = len(queryIndices)
        ans = [1] * k
        for i in range(k):
            idx = queryIndices[i]
            c = queryCharacters[i]
            if idx < l or idx > r:
                if c == s[idx]:
                    ans[i] = max_len
                    continue
                else:
                    pass
                # 不会写
            