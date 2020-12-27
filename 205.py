class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        values = set()
        for a, b in zip(s, t):
            if a in m:
                if m[a] != b:
                    return False
            else:
                if b in values:
                    return False
                m[a] = b
                values.add(b)
        return True


if __name__ == "__main__":
    s = Solution()
    print()
