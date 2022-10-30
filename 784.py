from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for c in s:
            if c.isalpha():
                tmp1 = [x + c.lower() for x in ans]
                tmp2 = [x + c.upper() for x in ans]
                ans = tmp1 + tmp2
            else:
                ans = [x + c for x in ans]
        return ans
