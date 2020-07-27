from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        idx_s = 0
        len_s = len(s)
        for char in t:
            if char == s[idx_s]:
                print(char, s[idx_s])
                idx_s += 1
                if idx_s == len_s:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    a = "acb"
    b = "ahbgdc"
    print(s.isSubsequence(a, b))