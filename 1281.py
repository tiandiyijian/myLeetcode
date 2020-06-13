class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        m = 1
        while n:
            mod = n % 10
            s += mod
            m *= mod
            n //= 10
        return m - s


if __name__ == "__main__":
    s = Solution()
    print()
