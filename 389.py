from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return list((Counter(t) - Counter(s)).keys())[0]
        tmp = 0
        for c in s:
            tmp ^= ord(c)
        for c in t:
            tmp ^= ord(c)
        return chr(tmp)


if __name__ == "__main__":
    s = Solution()
    print()
