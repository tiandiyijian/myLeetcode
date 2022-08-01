from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0:
            return ''
        if n & 1 == 0:
            return 'a' * (n - 1) + 'b'
        else:
            return 'a' * n
            # return self.generateTheString(n-1) + 'c'
