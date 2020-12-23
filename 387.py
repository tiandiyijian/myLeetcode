from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("leetcode"))
