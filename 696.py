class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        ans = 0
        i = 0
        while i < length:
            l = i
            while i < length - 1 and s[i+1] == s[i]:
                i += 1
            tmp_count = i - l + 1
            ans += min(tmp_count, count)
            count = tmp_count
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.countBinarySubstrings("00110"))
