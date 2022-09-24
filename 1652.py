from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            pre_sum = [0] * (n + k)
            for i in range(1, n + k):
                pre_sum[i] = pre_sum[i - 1] + code[i % n]

            for i in range(n):
                ans[i] = pre_sum[i + k] - pre_sum[i]
        else:
            post_sum = [0] * (n - k)
            for i in range(n - k - 2, -1, -1):
                post_sum[i] += post_sum[i + 1] + code[(i + k) % n]

            for i in range(n):
                ans[i] = post_sum[i] - post_sum[i - k]

        return ans
