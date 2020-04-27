class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        # MIN = (-1 << 31) // 10
        MAX = ((1 << 31) -1) // 10
        ans = 0
        sign = 1
        i = 0
        length = len(str)
        while i < length and str[i] == ' ': i += 1
        if i == length: return 0
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1
        # print(i)
        while i < length and '0' <= str[i] <= '9':
            num = int(str[i])
            print(ans, num)
            if sign == 1:
                if ans > MAX or (ans == MAX and num > 7): return (1 << 31) - 1
            else:
                if ans > MAX or (ans == MAX and num > 8): return -1 << 31
            ans = ans * 10 + num
            i += 1
        return ans * sign


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("2147483648"))