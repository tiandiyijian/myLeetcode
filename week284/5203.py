from typing import List


class Solution:

    def digArtifacts(self, n: int, artifacts: List[List[int]],
                     dig: List[List[int]]) -> int:
        dig_set = set((r, c) for r, c in dig)

        ans = 0
        for r1, c1, r2, c2 in artifacts:
            flag = False
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if (i, j) not in dig_set:
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                ans += 1

        return ans