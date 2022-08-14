class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = []
        left = '123456789'

        # cur = pattern[0]
        # i = 1
        # while i < n and pattern[i] == cur:
        #     i += 1
        # if cur == 'D':
        #     i += 1
        #     ans += sorted(left[:i], reverse=True)
        #     left = left[i:]
        # else:
        #     ans += sorted(left[:i])
        #     left = left[i:]

        i = 0
        while i < n:
            cur = pattern[i]
            j = i + 1
            while j < n and pattern[j] == cur:
                j += 1
            if cur == 'D':
                j += 1
                ans += sorted(left[: j - i], reverse=True)
                left = left[j - i :]
            else:
                ans += sorted(left[: j - i])
                left = left[j - i :]
            i = j

        if pattern[-1] == 'I':
            ans += left[0]

        return ''.join(ans)
