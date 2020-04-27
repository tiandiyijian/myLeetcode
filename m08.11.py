class Solution:
    def waysToChange(self, n: int) -> int:
        # ans = 0
        # for a in range(n // 25 + 1):
        #     sum1 = a * 25
        #     if sum1 == n:
        #         ans += 1
        #         break
        #     for b in range((n-sum1)//10 + 1):
        #         sum2 = sum1 + b * 10
        #         if sum2 == n:
        #             ans += 1
        #             # print(a, b)
        #             break
        #         for c in range((n-sum2)//5 + 1):
        #             sum3 = sum2 + c * 5
        #             if sum3 == n:
        #                 ans += 1
        #                 # print(a, b, c)
        #                 break
        #             # for d in range((n-sum1) + 1):
        #             #     if sum1 + d == n:
        #             #         ans += 1
        #             ans += 1
        #             # print(a, b, c, n-sum3)
        # return ans % 1000000007
        dp = [1] + [0] * n
        coins = [1, 5, 10, 25]
        for coin in coins:
            for i in range(coin,n+1):
                dp[i] += dp[i-coin]
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.waysToChange(25))