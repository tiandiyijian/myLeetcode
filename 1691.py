from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # 把堆叠想象成把小盒子装在大盒子里面
        # 所以可以直接选最长的边作为高
        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort()

        dp = [0] * n
        dp[0] = cuboids[0][-1]
        for i in range(1, n):
            w2, l2, h2 = cuboids[i]
            dp[i] = h2
            for j, (w1, l1, h1) in enumerate(cuboids[:i]):
                if w1 <= w2 and l1 <= l2 and h1 <= h2:
                    dp[i] = max(dp[i], dp[j] + h2)

        return max(dp)
