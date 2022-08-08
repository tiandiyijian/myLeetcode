class Solution:
    # 参考题解：https://leetcode.cn/problems/special-binary-string/solution/onlogn-by-vclip-eyy8/
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        left = 0
        cnt = 0
        subs = []

        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append('1' + self.makeLargestSpecial(s[left+1:i]) + '0')
                    left = i + 1

        subs.sort(reverse=True)
        
        return ''.join(subs)