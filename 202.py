class Solution:
    def isHappy(self, n: int) -> bool:
        history = set()
        while n != 1:
            tmp = 0
            history.add(n)
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
            if n in history:
                return False
        return True



if __name__ == "__main__":
    s = Solution()
    print()