from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        push = "Push"
        pop = "Pop"

        cur = 1
        ans = []
        for t in target:
            while cur != t:
                ans.append(push)
                ans.append(pop)
                cur += 1
            ans.append(push)
            cur += 1

        return ans
