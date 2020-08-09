from typing import List


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def judge(s):
            if len(s) > 1 and s[0] == '0':
                return False
            return 0 <= int(s) <= 255
        ans = []
        length = len(s)
        if length > 12 or length < 4:
            return ans
        for i in range(1, 4):
            first = s[0:i]
            if judge(first):
                for j in range(i+1, 7):
                    if j > length - 2:
                        break
                    second = s[i:j]
                    if judge(second):
                        for k in range(j+1, 10):
                            if k > length - 1:
                                break
                            third = s[j:k]
                            fourth = s[k:length]
                            if judge(third) and judge(fourth):
                                ans.append(first+'.'+second+'.'+third+'.'+fourth)
        print(ans)
        return ans

    def restoreIpAddresses1(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        ans = []
        def helper(s, count=0, pre=''):
            nonlocal ans
            if count == 3:
                if s[0] == '0' and len(s) > 1:
                    return
                if int(s) < 256:
                    # print(s, pre)
                    ans.append(pre+s)
                return
            length = len(s)
            if s[0] == '0':
                helper(s[1:], count + 1, pre + s[0] + '.')
                return
            for i in range(length - (4- count) + 1):
                if 0 < int(s[:i+1]) < 256:
                    helper(s[i+1:], count + 1, pre+s[:i+1] + '.')
        
        helper(s)
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.restoreIpAddresses1("010010"))