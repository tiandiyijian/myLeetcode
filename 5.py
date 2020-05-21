class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        self.left = 0
        self.max_len = 0
        def expand_str(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r +=1
            if r - l - 1 > self.max_len:
                self.left = l + 1
                self.max_len = r - l - 1
                print(self.left, self.max_len)
        for i in range(len(s)-1):
            expand_str(i, i)
            expand_str(i, i+1)
        print(self.left, self.max_len)
        return s[self.left: self.left + self.max_len]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ans = ''
        for size in range(1, len(s) + 1):
            for left in range(len(s)):
                right = left + size - 1
                if right > len(s) - 1:
                    break
                if size == 1:
                    dp[left][right] = True
                elif size == 2:
                    dp[left][right] = s[left] == s[right]
                else:
                    dp[left][right] = dp[left+1][right-1] and s[left] == s[right]
                if dp[left][right] and size > len(ans):
                    ans = s[left: right + 1]
        for r in dp:
            print(r)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('babad'))        