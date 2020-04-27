from typing import List

class Solution:
   def minimumLengthEncoding(self, words: List[str]) -> int:
         if not words:
            return 0
         words1 = set(words)
         for word in words:
            for i in range(1, len(word)):
               words1.discard(word[i:])
         return sum(len(word) + 1 for word in words1)

if __name__ == "__main__":
   s = Solution()
   print(s.minimumLengthEncoding(["t"]))