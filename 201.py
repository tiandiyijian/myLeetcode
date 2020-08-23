class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= (n-1)
        return n


if __name__ == "__main__":
    s = Solution()
    print(s.rangeBitwiseAnd(5, 7))
