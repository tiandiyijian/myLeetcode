from typing import List


class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        self.mem = {"":True}
        for str in wordDict:
            self.mem[str] = True
        return self.judge(s)

    def judge(self, s):
        if  s in self.mem:
            return self.mem[s]
        for i in range(1, len(s)):
            r = s[i : ]
            l = s[0 : i]
            # if i == 4:
            #     print(l, r)
            #     print(self.mem)
            #     print(r in self.mem and self.mem[r] and l in self.mem and self.mem[l])
            #if r in self.mem and self.mem[r] and l in self.mem and self.mem[l]:
            #不可以这样，这样的话一方面是学习不到新东西，因为根本就没递归，另一方面是wordDict里的单词不可以重复使用，根本就是错的，可以拿applepenapple做实验
            if r in self.mem and self.mem[r] and self.judge(s[0:i]):
                self.mem[s] = True
                return True
        self.mem[s] = False
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.ans = False
        def helper(start):
            if s[start:] in wordDict:
                self.ans = True
                return
            for i in range(start+1, len(s)):
                if s[start:i] in wordDict:
                    print(s[start:i])
                    helper(i)
        helper(0)
        return self.ans


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [0]
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(len(mem)):
                if s[mem[j]:i] in wordDict:
                    mem.append(i)
                    break
        return mem[-1] == len(s)


if __name__ == '__main__':
    a = Solution()
    str = 'applepenapple'
    wordDict = ["apple", "pen"]
    print(a.wordBreak(str, wordDict))
