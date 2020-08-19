class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        ans = length
        for i in range(length - 1):
            dp[i][i] = 1
            if s[i] == s[i + 1]:
                dp[i][i+1] = 1
                ans += 1
        dp[length - 1][length - 1] = 1
        for size in range(3, length + 1):
            for left in range(length - size + 1):
                right = left + size - 1
                if dp[left + 1][right - 1] and s[left] == s[right]:
                    dp[left][right] = 1
                    ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings('a'))
