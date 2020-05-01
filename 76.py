from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        lens = len(s)
        i = j = 0
        lenUnique = len(need)
        tmpLen = 0
        ans = (float('inf'), None, None)
        while j < lens:
            if s[j] in need:
                window[s[j]] = window.get(s[j], 0) + 1
                if window[s[j]] == need[s[j]]:
                    tmpLen += 1
            while i <= j and tmpLen == lenUnique:
                print(i, j)
                if j - i + 1 < ans[0]:
                    ans = (j - i + 1, i, j)
                if s[i] in window:
                    window[s[i]] -= 1
                    if window[s[i]] < need[s[i]]:
                        tmpLen -= 1
                i += 1
            j += 1
        return s[ans[1]: ans[2]+1] if ans[0] != float('inf') else ''

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("aaaaaaaaaaaabbbbbcdd", "abbbbbcdd"))