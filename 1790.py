class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        i1 = i2 = -1

        for i in range(n):
            if s1[i] != s2[i]:
                if i1 < 0:
                    i1 = i
                elif i2 < 0:
                    i2 = i
                    if not (s1[i1] == s2[i2] and s1[i2] == s2[i1]):
                        return False
                else:
                    return False

        return i1 < 0 or i2 >= 0
