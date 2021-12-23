import random

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # 生成两个进制
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        # 生成两个模
        mod1, mod2 = random.randint(10**9+7, 2**31-1), random.randint(10**9+7, 2**31-1)
        arr = [ord(c) - ord('a') for c in s]
        n = len(arr)

        def check(m):
            aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
            h1 = h2 = 0
            for i in range(m):
                h1 = (h1 * a1 + arr[i]) % mod1
                h2 = (h2 * a2 + arr[i]) % mod2
            seen = {(h1, h2)}
            for start in range(1, n - m + 1):
                h1 = (h1 * a1 - arr[start-1] * aL1 + arr[start+m-1]) % mod1
                h2 = (h2 * a2 - arr[start-1] * aL2 + arr[start+m-1]) % mod2
                if (h1, h2) in seen:
                    return start
                seen.add((h1, h2))
            return -1
        
        low, high = 0, n-1
        length, start = 0, -1
        while low <= high:
            mid = low + (high - low + 1) // 2
            # print(low, high, mid)
            idx = check(mid)
            if idx != -1:
                low = mid + 1
                length = mid
                start = idx
            else:
                high = mid - 1
        return s[start:start+length] if start != -1 else ""

print(Solution().longestDupSubstring("banana"))