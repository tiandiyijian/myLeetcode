from collections import defaultdict
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        p = list(range(n+1))
        sz = [1] * (n+1)

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        def union(i, j):
            if find(i) != find(j):
                sz[find(i)] += sz[find(j)]
                p[find(j)] = p[find(i)]
                nonlocal ans
                ans = max(ans, sz[find(i)])


        mp = defaultdict(list)
        for i, num in enumerate(nums):
            j = 2
            # 分解质因数
            # 刚开始我想到了分解因数但是又感觉因数太多不太可行
            # 后来看宫水三叶发现可以分解质因数
            while j * j <= num:
                if num % j == 0:
                    mp[j].append(i)
                    if j != num // j:
                        mp[num // j].append(i)
                while num % j == 0:
                    num //= j
                j += 1
            if num > 1:
                mp[num].append(i)
            print(num, mp)
        
        for k, l in mp.items():
            for i in range(1, len(l)):
                union(l[0], l[i])
            ans = max(ans, sz[l[0]])
            print(ans)
            print(k, l)
            print(p)
            print(sz)
        
        print(mp)
        print(p)
        print(sz)
        
        return ans
        

nums = [20,50,9,63]
nums = [4,6,15,35]
print(Solution().largestComponentSize(nums))