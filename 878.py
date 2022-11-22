import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm()
        l = max(a, b)
        r = n * a * b
        while l < r:
            mid = (l + r) >> 1
            cnt = mid // a + mid // b - mid // lcm
            if cnt < n:
                l = mid + 1
            else:
                r = mid
        return r