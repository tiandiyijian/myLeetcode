class Solution:
   def gcdOfStrings(self, str1: str, str2: str) -> str:
      def canDiv(str1, str2):
         if len(str1) % len(str2):
            return False
         return str2 * (len(str1) // len(str2)) == str1
      ans = ''
      for i in range(min(len(str1), len(str2))):
         if str1[i] != str2[i]:
            return ans
         elif canDiv(str1, str1[:i+1]) and canDiv(str2, str2[:i+1]):
            ans = str1[:i+1]
      return ans

if __name__ == "__main__":
   s = Solution()
   print(s.gcdOfStrings('ababab', 'abc'))