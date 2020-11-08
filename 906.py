from typing import List


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L, R = int(L), int(R)
        magic = 10 ** 6
        ans = 0

        def check_palindrome(num):
            tmp = str(num)
            length = len(tmp) // 2
            return tmp[:length] == tmp[-1:-1-length:-1]
            # if len(tmp) & 1: # odd
            #     return tmp[]

        def build_palindrome(num):
            tmp = str(num)
            a = tmp + tmp[-2::-1]
            b = tmp + tmp[::-1]
            return int(a), int(b)

        # print(check_palindrome(22))
        # print(build_palindrome(1))

        for i in range(1, magic):
            a, b = build_palindrome(i)
            # print(a, b)
            a = a ** 2
            b = b ** 2
            if b < L:
                continue
            if a > R:
                return ans
            if L <= a <= R and check_palindrome(a):
                print(a)
                ans += 1
            if L <= b <= R and check_palindrome(b):
                print(b)
                ans += 1
        print(a, b)
            

if __name__ == "__main__":
    s = Solution()
    L = "38455498359"
    R = "999999999999999999"
    print(s.superpalindromesInRange(L, R))