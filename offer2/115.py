from typing import List


class Solution:
    def sequenceReconstruction(
        self, nums: List[int], sequences: List[List[int]]
    ) -> bool:
        n = len(nums)

        g = [[] for _ in range(n)]
        degree = [0] * (n)
        cnt = n
        
        for s in sequences:
            for i in range(len(s) - 1):
                g[s[i] - 1].append(s[i + 1] - 1)
                degree[s[i + 1] - 1] += 1
                if degree[s[i + 1] - 1] == 1:
                    cnt -= 1
        
        if cnt != 1:
            return False
        
        for num in nums:
            if degree[num - 1] > 0:
                return False
            cnt = 0
            for nei in g[num - 1]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    cnt += 1
                    if cnt > 1:
                        return False

        return True


nums = [1, 2, 3]
seq = [[1, 2], [1, 3]]
nums = [4, 1, 5, 2, 6, 3]
seq = [[5, 2, 6, 3], [4, 1, 5, 2]]
print(Solution().sequenceReconstruction(nums, seq))
