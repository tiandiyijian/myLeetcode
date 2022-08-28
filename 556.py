class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        n = len(s)
        for i in range(n - 1, 0, -1):
            if s[i] > s[i - 1]:
                for j in range(i, n):
                    if s[j] <= s[i - 1]:
                        s[i - 1], s[j - 1] = s[j - 1], s[i - 1]
                        s[i:] = sorted(s[i:])
                        break
                else:
                    s[i - 1], s[-1] = s[-1], s[i - 1]
                    s[i:] = sorted(s[i:])
                ans = int(''.join(s))
                return ans if ans <= (1 << 31) - 1 else -1
        return -1


print(Solution().nextGreaterElement(2147483476))
