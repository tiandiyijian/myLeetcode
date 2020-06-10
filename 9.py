class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i, j = 0, len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        post = 0
        while x > post:
            post = post * 10 + x % 10
            x //= 10
        # if x < post:
        #     return x == post // 10
        return x == post or x == post // 10


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(56765))
