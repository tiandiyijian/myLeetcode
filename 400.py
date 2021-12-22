class Solution:
    def findNthDigit(self, n: int) -> int:
        x = 1
        while True:
            if (tmp := 9 * x * pow(10, x-1)) < n:
                n -= tmp
                x += 1
            else:
                idx = (n-1) // x
                bit = (n-1) % x
                num = pow(10, x-1) + idx
                # print(n, idx, num, bit)
                # return int(str(num)[bit])
                return num // pow(10, x - 1 - bit) % 10