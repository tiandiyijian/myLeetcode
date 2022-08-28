class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # 想简单点
        # 第一位数有9种选择
        # 第二位数有8种选择
        # 第三位数有7种选择
        # ...
        if n == 0:
            return 1
        ans = 10
        pre = 9
        for i in range(2, n+1):
            pre = pre * (10 - i + 1)
            ans += pre
        return ans