from collections import deque
from typing import List



class Solution:

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        halfLength = (intLength + 1) >> 1
        base = pow(10, halfLength-1)
        maxBase = pow(10, intLength-1)
        def getq(i):
            if i > 9 * base:
                return -1
            curBase = base
            i -= 1
            num = 0
            l = [0] * halfLength
            l[0] = 1
            l_idx = 0
            # 完全多此一举，第i大的数就是i啊艹
            while i > 0:
                num += ((i // curBase)) * curBase
                l[l_idx] += (i // curBase)
                l_idx += 1
                i %= curBase
                curBase //= 10
            # print(l)
            Base = maxBase
            reverseBase = 1
            ans = 0
            for i in range(halfLength if intLength & 1 == 0 else halfLength - 1):
                ans += Base * l[i]
                ans += reverseBase * l[i]
                Base //= 10
                reverseBase *= 10
            if intLength & 1 == 1:
                ans += l[-1] * Base
            # print(ans)
            return ans
            return base + num
        
        return [getq(q) for q in queries]

queries = [1,2,3,4,5, 6, 90]
intLength = 4
print(Solution().kthPalindrome(queries, intLength))