class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        r = s[::-1]
        for i in range(len(r)):
            if s.startswith(r[i:]):
                return r[:i] + s

    def shortestPalindrome2(self, s: str) -> str:
        S = s + '#' + s[::-1]

        def kmp(s):
            next = [0] * len(s)
            i = 1
            tmp_len = 0
            while i < len(s):
                if s[i] == s[tmp_len]:
                    tmp_len += 1
                    next[i] = tmp_len
                    i += 1
                else:
                    if tmp_len == 0:
                        next[i] = 0
                        i += 1
                    else:
                        tmp_len = next[tmp_len - 1]
            return next

        next = kmp(S)
        return s[next[-1]:][::-1] + s

if __name__ == "__main__":
    s = Solution()
    print(s.shortestPalindrome2('ab'))
