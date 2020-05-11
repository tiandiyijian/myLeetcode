class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            return self.myPow(x, n//2) ** 2 if n & 1 == 0 else x * self.myPow(x, n//2) ** 2


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2.0, 4))
