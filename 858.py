from math import gcd

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = p * q // gcd(p, q)    
        m = g // p
        k = g // q
        # k = 1
        # m = 0
        # while (q/p*k) % 1 != 0:
        #     k += 1
        # m = int(q / p * k)
        # m = int(q / p * k)
        # print(m, k)
        if m & 1:
            if k & 1:
                return 1
            else:
                return 2
        else:
            return 0



if __name__ == "__main__":
    s = Solution()
    print(s.mirrorReflection(2, 1))