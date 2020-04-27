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
        

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('cbbd'))        