class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s[:len(s)//2] == s[:-(len(s)//2+1):-1]
        # def trans(s):
        #     num = ord(s)
        #     if ord('a') <= num <= ord('z') or ord('0') <= num <= ord('9'):
        #         return True
        #     elif ord('A') <= num <= ord('Z'):
        #         return True
        #     else:
        #         return False
        # s = filter(trans, s)
        # # print(s)
        # s = ''.join(s)
        # # print(s)
        # s = s.lower()
        # return s[:len(s)//2] == s[:-(len(s)//2+1):-1]


if __name__ == "__main__":
    s = Solution()
    S = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(S))
