class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        f = [[0] * 10 for _ in range(10)]
        for i in range(1, 10):
            for j in range(i, 10):
                cur = 1
                for k in range(i, j + 1):
                    cur *= k
                f[i][j] = cur

        def dp(x):
            t = x
            nums = []
            while t > 0:
                nums.append(t % 10)
                t //= 10

            n = len(nums)
            if n <= 1:
                return x + 1

            ans = 0
            choosed = 0
            s = 0
            # 位数与x相同的数字
            # 每次都寻找当前最高位可使用的比最高位小的数字
            # 然后固定最高位和x相同继续进行下一轮寻找
            for i in range(n - 1, -1, -1):
                cur = nums[i]
                cnt = 0
                for j in range(cur - 1, -1, -1):
                    if i == n - 1 and j == 0:
                        continue
                    if (s >> j) & 1 == 0:
                        cnt += 1

                choosed += 1
                r = 10 - choosed
                l = r - (n - choosed) + 1
                ans += cnt * f[l][r] if l <= r else cnt

                # print(i, cnt, l, r, ans, s)
                if (s >> cur) & 1 == 1:
                    # 当前位与前面的重复了
                    # 该前缀不能作为合法前缀
                    break
                s |= 1 << cur
                if i == 0:
                    # 到最后一轮也没有break说明x本身也合法
                    ans += 1

            # 位数小于x的数字
            ans += 10  # 0-9
            pre = 9  # 第一位数字不能是0所以只有9钟选择
            for i in range(2, n):
                pre = pre * (10 - i + 1)
                ans += pre
            return ans

        return n + 1 - dp(n)
