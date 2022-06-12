from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        total = sum(cookies)
        avg = total / k
        cookies.sort(reverse=True)

        ans = float('inf')
        own = [0] * k
        def dfs(i):
            if i == n:
                nonlocal ans
                ans = min(ans, max(own))
                return
            for j in range(k):
                if own[j] < avg:
                    own[j] += cookies[i]
                    dfs(i+1)
                    own[j] -= cookies[i]
        
        dfs(0)
        return ans


cookies = [8,15,10,20,8]
k = 2
cookies = [6,1,3,2,2,4,1,2]
k = 3
print(Solution().distributeCookies(cookies, k))