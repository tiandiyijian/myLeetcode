from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp1 = {v: i for i, v in enumerate(list1)}
        # mp2 = {v :i for i, v in enumerate(list2)}

        ans = []
        min_sum = 2000
        for i, v in enumerate(list2):
            if v not in mp1:
                continue
            j = mp1[v]
            if i + j == min_sum:
                ans.append(v)
            elif i + j < min_sum:
                min_sum = i + j
                ans = [v]
        return ans
