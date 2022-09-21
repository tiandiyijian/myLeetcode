from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        if s1 == s2:
            return 0

        vis = set([s1])
        q = deque([(s1, 0)])
        while q:
            s, step = q.popleft()
            for i in range(n):
                if s[i] == s2[i]:
                    continue
                for j in range(i + 1, n):
                    if s[j] != s2[i]:
                        continue
                    new_s = s[:i] + s[j] + s[i + 1 : j] + s[i] + s[j + 1 :]
                    if new_s == s2:
                        return step + 1
                    if new_s not in vis:
                        vis.add(new_s)
                        q.append((new_s, step + 1))
                # 一次只变一个
                break
