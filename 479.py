class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        maxNum = 10 ** n - 1
        # print(maxNum)
        for n in range(maxNum, -1, -1):
            tmp = n
            while tmp > 0:
                n = n * 10 + tmp % 10
                tmp //= 10
            for j in range(maxNum, int(n**0.5), -1):
                if n % j == 0 and n // j < maxNum:
                    # print(n, j)
                    return n % 1337
        