class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                # ans = max(ans, count)
            else:
                ans = max(ans, count)
                count = 1
        return max(ans, count)


if __name__ == "__main__":
    s = Solution()
    print(s.maxPower('abbcccddddeeeeedcba'))
