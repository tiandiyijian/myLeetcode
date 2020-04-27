from typing import List

class Solution:
      def surfaceArea(self, grid: List[List[int]]) -> int:
         if not grid or not grid[0]:
            return 0
         numcubes = 0
         numblocks = 0
         for i in range(len(grid)):
            for j in range(len(grid[0])):
               if grid[i][j] > 0:
                  numcubes += grid[i][j]
                  numblocks += grid[i][j] - 1
                  if i > 0:
                     numblocks += min(grid[i-1][j], grid[i][j])
                  if j > 0:
                     numblocks += min(grid[i][j-1], grid[i][j])
         return numcubes * 6 - numblocks * 2

if __name__ == "__main__":
   s = Solution()
   print(s.surfaceArea([[0,1,1],[1,1,1],[1,1,1]]))