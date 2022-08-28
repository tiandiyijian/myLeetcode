from typing import List


class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def selfDivide(num):
            a = num
            while a > 0:
                b = a % 10
                a //= 10
                if b == 0 or num % b != 0:
                    return False
            return True

        return [i for i in range(left, right + 1) if selfDivide(i)]
