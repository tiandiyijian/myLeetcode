from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = min(n, 2)

        l = 0
        categories = {fruits[0]: 1}
        for r in range(1, n):
            if fruits[r] not in categories and len(categories) == 2:
                while len(categories) == 2:
                    categories[fruits[l]] -= 1
                    if categories[fruits[l]] == 0:
                        del categories[fruits[l]]
                    l += 1
                categories[fruits[r]] = 1
            else:
                if fruits[r] in categories:
                    categories[fruits[r]] += 1
                else:
                    categories[fruits[r]] = 1
            ans = max(ans, r - l + 1)

        return ans
