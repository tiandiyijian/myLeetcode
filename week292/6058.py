from functools import lru_cache


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        fourCharKeys = '79'
        mod = 10**9 + 7

        @lru_cache()
        def helper(key_cnt, char_cnt):
            dp = [0] * (key_cnt + char_cnt)
            dp[char_cnt-1] = 1
            if char_cnt == 3:
                for i in range(char_cnt, len(dp)):
                    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            elif char_cnt == 4:
                for i in range(char_cnt, len(dp)):
                    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
            print(dp)
            return dp[-1]

        n = len(pressedKeys)
        i = 0
        ans = 1
        while i < n:
            j = i + 1
            while j < n and pressedKeys[j] == pressedKeys[i]:
                j += 1
            ans = (ans * helper(j - i, 4 if pressedKeys[i] in fourCharKeys else 3) % mod) % mod
            i = j
        
        return ans % mod


keys = "444444444444444444444444444444448888888888888888999999999999333333333333333366666666666666662222222222222222666666666666666633333333333333338888888888888888222222222222222244444444444444448888888888888222222222222222288888888888889999999999999999333333333444444664"
print(Solution().countTexts(keys))