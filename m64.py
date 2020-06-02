class Solution:
    def sumNums(self, n: int) -> int:
        return n and n + self.sumNums(n-1)


if __name__ == "__main__":
    s = Solution()
    print(s.sumNums(5))
