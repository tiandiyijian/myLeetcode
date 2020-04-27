
class Solution:
    def reverseWords(self, s: str) -> str:
        # words = []
        # tmp = ""
        # for i in s:
        #     if i == " ":
        #         if tmp != "":
        #             words.append(tmp)
        #             tmp = ""
        #         else:
        #             continue
        #     else:
        #         tmp += i
        # if tmp: words.append(tmp)
        # return " ".join(words[::-1])
        words = s.split()
        return " ".join(words[::-1])



if __name__ == "__main__":
   s = Solution()
   print(s.reverseWords("the sky is blue"))