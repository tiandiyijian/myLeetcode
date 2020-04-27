from typing import List

class Solution:
   def canThreePartsEqualSum(self, A: List[int]) -> bool:
      length = len(A)
      if length < 3: return False
      for i in range(1, length):
         A[i] += A[i-1]
      if A[length-1] % 3:
         return False
      times = 1
      target = A[length-1] // 3
      for i in range(length-1):
         if A[i] == times * target:
            times += 1
            # print(i)
            if times == 3:
               return True
      return False
      

if __name__ == "__main__":
   s = Solution()
   print(s.canThreePartsEqualSum([6,1,1,13,-1,0,-10,20]))