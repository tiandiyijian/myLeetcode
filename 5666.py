from typing import List


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        judge = [[False] * n for _ in range(n)]
        for i in range(n-1):
            judge[i][i] = True
            judge[i][i+1] = (s[i] == s[i+1])
        judge[n-1][n-1] = True
        for size in range(2, n):
            for l in range(n):
                r = l + size
                if r > n - 1:
                    break
                judge[l][r] = judge[l + 1][r - 1] and s[l] == s[r]

        pre = []
        post = []

        for i in range(n):
            if judge[0][i]:
                pre.append(i)
            if judge[n - i - 1][n - 1]:
                post.append(n - i - 1)
        for left in pre:
            for right in post:
                if left + 1 >= right:
                    break
                if judge[left+1][right-1]:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    string = "juchzcedhfesefhdeczhcujzzvbmoeombv"
    print(s.checkPartitioning(string))
