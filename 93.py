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

if __name__ == '__main__':
    a = Solution()
    a.restoreIpAddresses('123234124234')