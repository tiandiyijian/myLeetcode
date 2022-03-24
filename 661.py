from typing import List


class Solution:

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt = 0
                for p in range(i - 1, i + 2):
                    for q in range(j - 1, j + 2):
                        if 0 <= p < m and 0 <= q < n:
                            cnt += 1
                            ans[i][j] += img[p][q]
                ans[i][j] //= cnt
        return ans

img = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().imageSmoother(img))