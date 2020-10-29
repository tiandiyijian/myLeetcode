class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2**(n-1):
            return ''

        def getChar(idx, current):
            happy = 'abc'
            happy = happy.replace(current, '')
            return happy[idx]

        ans = ''
        num = 2**(n-1)
        k -= 1
        current = ''
        while num > 0:
            idx = k // num
            current = getChar(idx, current)
            ans += current
            k = k % num
            num //= 2
            # n -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.getHappyString(3, 4))
