from typing import List



class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # 我傻逼了, 直接暴力就行了
        s, n = set(), len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                    if cnt > k:
                        break
                s.add(tuple(nums[i: j + 1]))
        return len(s)