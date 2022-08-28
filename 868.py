class Solution:

    def binaryGap(self, n: int) -> int:
        pre = -1
        maxGap = 0
        i = 0
        while n > 0:
            if n & 1 == 1:
                if pre < 0:
                    pre = i
                else:
                    maxGap = max(maxGap, i - pre)
                    pre = i
            n >>= 1
            i += 1

        return maxGap