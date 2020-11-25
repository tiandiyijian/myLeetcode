class Solution:
    def sortString(self, s: str) -> str:
        ans = ''
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        pre_len = -1
        while len(ans) > pre_len:
            pre_len = len(ans)
            for i in range(26):
                if count[i] > 0:
                    ans += chr(i + ord('a'))
                    count[i] -= 1
            for i in range(25, -1, -1):
                if count[i] > 0:
                    ans += chr(i + ord('a'))
                    count[i] -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
