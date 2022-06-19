class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        cur = 0
        size = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                size += 1
            else:
                nxt = (1 << size) + cur
                if nxt > k:
                    break
                cur = nxt
                size += 1

        # print(i, cur, size)
        for j in range(i):
            if s[j] == '0':
                size += 1

        return size


s = "1001010"
k = 5
s = "00101001"
k = 1
print(Solution().longestSubsequence(s, k))
