from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        m, n = len(image), len(image[0])
        def dfs(x, y):
            image[x][y] = newColor
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if image[nx][ny] == color:
                        dfs(nx, ny)
        
        dfs(sr, sc)
        return image

if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[0,0,0],[0,1,1]], 1, 1, 1))