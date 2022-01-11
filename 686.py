import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 如何更好地理解和掌握 KMP 算法? - 阮行止的回答 - 知乎https://www.zhihu.com/question/21923021/answer/1032665486
        def kmp(q, p):
            m, n = len(q), len(p)
            next = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and p[i] != p[j]:
                    j = next[j-1]
                if p[i] == p[j]:
                    j += 1
                next[i] = j
            i = j = 0
            while i - j < m:
                while j > 0 and q[i % m] != p[j]:
                    j = next[j-1]
                if q[i % m] == p[j]:
                    j += 1
                    if j == n:
                        return i - j + 1
                i += 1
            return -1
        
        idx = kmp(a, b)
        if idx == -1:
            return -1
        m, n = len(a), len(b)
        if m - idx >= n:
            return 1
        return math.ceil((n - (m - idx)) / m) + 1

a = "aaaaaaaaaaaaaaaaaaaaaab"
b = "ba"
print(Solution().repeatedStringMatch(a, b))