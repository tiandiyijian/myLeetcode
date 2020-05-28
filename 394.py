import collections

class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        stack = collections.deque()
        i = 0
        while i < len(s):
            if '1' <= s[i] <= '9':
                start = i
                while '0' <= s[i+1] <= '9':
                    i += 1
                stack.append(int(s[start:i+1]))
            elif s[i] == '[':
                stack.append(s[i])
            elif s[i] == ']':
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop() # '['
                stack[-1] = stack[-1] * tmp
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)

class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(i):
            ans = ''
            while i < len(s):
                # print(i)
                if '0' <= s[i] <= '9':
                    start = i
                    while '0' <= s[i+1] <= '9':
                        i += 1
                    multi = int(s[start:i+1])
                    i += 1
                    if s[i] == '[':
                        i, tmp = dfs(i+1)
                        ans += multi * tmp
                elif s[i] == ']':
                    return i+1, ans
                else:
                    ans += s[i]
                    i += 1
                
            return i, ans
        return dfs(0)[1]



if __name__ == "__main__":
    s = Solution()
    print(s.decodeString('3[a2[c]]'))