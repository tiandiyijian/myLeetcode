class Solution:
    def mySqrt(self, x: int) -> int:
        s = x
        while s ** 2 > x:
            s = (s + x // s) // 2
        return s

class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        while i <= j:
            mid = (i + j) // 2
            num = mid ** 2
            if num == x:
                return mid
            elif num > x:
                j = mid - 1
            else:
                i = mid + 1
        return j


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(8))