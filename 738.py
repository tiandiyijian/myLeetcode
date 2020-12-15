class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        digits = list(str(N))
        i = 1
        while i < len(digits) and digits[i-1] <= digits[i]:
            i += 1
        # print(i)
        if i == len(digits):
            return N
        while i > 0 and digits[i-1] > digits[i]:
            digits[i-1] = chr(ord(digits[i-1]) - 1)
            i -= 1
        i += 1
        while i < len(digits):
            digits[i] = '9'
            i += 1
        # print(digits)
        return int(''.join(digits))




if __name__ == "__main__":
    s = Solution()
    print(s.monotoneIncreasingDigits(10))