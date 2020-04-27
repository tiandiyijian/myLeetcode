class Solution:
    def climbStairs(self, n: int) -> int:
        # res = [1, 2]
        # for i in range(2, n):
        #     res.append(res[i-2] + res[i-1])
        # return res[n-1]
        if n < 3:
            return n
        a = 1
        b = 2
        ans = 0
        for _ in range(n-2):
            ans = a + b
            a, b = b, ans
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(4))