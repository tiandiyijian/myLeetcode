class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        half = len(s) // 2
        if s[:half] == s[-1:-1-half:-1]:
            return 1
        return 2


if __name__ == "__main__":
    s = Solution()
    print()
