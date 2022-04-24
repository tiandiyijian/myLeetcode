from typing import List
from bisect import bisect_left

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 注意到rectangles中高度的最大值为100
        
        height = [[] for _ in range(101)]
        for l, h in rectangles:
            height[h].append(l)
        
        for i in range(101):
            height[i].sort()
        
        n = len(points)
        ans = [0] * n
        for i in range(n):
            for h in range(points[i][1], 101):
                if height[h]:
                    first = bisect_left(height[h], points[i][0])
                    ans[i] += len(height[h]) - first
        
        return ans
    
    def countRectangles1(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # 贴一个大佬的解法
        # 刚开始我也在想能不能DP可惜没想到
        # 这种边更新DP数组边更新ans数组的方法妙啊
        rectangles.sort()
        rectangles.reverse()
        queries = []
        for i, p in enumerate(points):
            queries.append((p[0], p[1], i))
        queries.sort()
        queries.reverse()
        dp = [0] * 105
        ans = [0] * len(points)
        pp = 0
        for px, py, i in queries:
            while pp < len(rectangles) and rectangles[pp][0] >= px:
                for j in range(rectangles[pp][1] + 1):
                    dp[j] += 1
                pp += 1
            ans[i] = dp[py]
        return ans


rectangles = [[1,2],[2,3],[2,5]]
points = [[2,1],[1,4]]
print(Solution().countRectangles(rectangles, points))
