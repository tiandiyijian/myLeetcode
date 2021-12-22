from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l, r = 0, len(plants) - 1
        ans = 0
        currentA = capacityA
        currentB = capacityB
        def helper(i, capacity, current):
            if plants[i] <= current:
                current -= plants[i]
                return current
            nonlocal ans
            ans += 1
            # print(i, ans)
            return capacity - plants[i]
            # return 
        while l < r:
            currentA = helper(l, capacityA, currentA)
            currentB = helper(r, capacityB, currentB)
            l += 1
            r -= 1
        if l == r:
            if currentA < currentB:
                currentB = helper(r, capacityB, currentB)
            else:
                currentA = helper(l, capacityA, currentA)
        return ans

p = [1,2,4,4,5]

print(Solution().minimumRefill(p, 6, 5))