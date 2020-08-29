class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def get_next(s):
            nxt = [0]
            i = 1
            now = 0
            while i < len(s):
                if s[i] == s[now]:
                    now += 1
                    nxt.append(now)
                    i += 1
                elif now > 0:
                    now = nxt[now-1]
                else:
                    nxt.append(0)
                    i += 1
            return nxt

        nxt = get_next(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            elif j > 0:
                j = nxt[j-1]
            else:
                i += 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr('ly', 'l'))
