class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        n_segment = 0
        i = 0
        while i < n:
            if s[i] == "1":
                n_segment += 1
                if n_segment > 1:
                    return False
                for j in range(i + 1, n):
                    if s[j] != "1":
                        i = j
                        break
                else:
                    break
            else:
                i += 1

        return n_segment <= 1
