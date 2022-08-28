from typing import List


class Solution:

    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [-1] * n

        pre = -1
        for i in range(n):
            if s[i] == c:
                ans[:i + 1] = list(range(i, -1, -1))
                pre = i
                break
        for i in range(n):
            if s[i] == c:
                if pre + 1 == i:
                    pre = i
                    ans[i] = 0
                    continue
                ans[i] = 0
                mid = (pre + i) >> 1
                for j in range(pre + 1, mid + 1):
                    ans[j] = j - pre
                for j in range(mid + 1, i):
                    ans[j] = i - j
                pre = i
                # print(i, ans)

        if pre != n - 1:
            for j in range(pre + 1, n):
                ans[j] = j - pre

        return ans