class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = len(s)
        window = set()
        i = j = 0
        ans = 0
        while j < lens:
            char = s[j]

            if char in window:
                window.discard(s[i])
                i += 1
            else:
                window.add(char)
                j += 1
                ans = max(ans, j - i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('pwwkew'))
