class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a+b
        return b


if __name__ == "__main__":
    s = Solution()
    print()
