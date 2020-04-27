class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # def help(K, N):
        #     if K == 1:
        #         return N
        #     if N % 2 == 1:
        #         return 1 + help(K - 1, N // 2)
        #     else:
        #         return 1 + max(help(K - 1, N // 2 - 1), help(K, N // 2))
        # return help(K, N)
        mem = {}
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
            if (K, N) in mem:
                return mem[(K, N)]
            lo, hi = 1, N
            ans = N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    ans = min(ans, broken + 1)
                else:
                    lo = mid + 1
                    ans = min(ans, not_broken + 1)
            mem[(K, N)] = ans
            # print(ans)
            return ans
        return dp(K, N)

if __name__ == "__main__":
    s = Solution()
    print(s.superEggDrop(3, 14))
