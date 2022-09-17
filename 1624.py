class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        pre = [None] * 26
        ans = -1
        for i, c in enumerate(s):
            idx = ord(c) - ord("a")
            if pre[idx] is not None:
                ans = max(ans, i - pre[idx] - 1)
            else:
                pre[idx] = i

        return ans
