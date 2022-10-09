class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # stack = []
        # for i in S:
        #     if i == '(':
        #         stack.append(i)
        #     else:
        #         if stack[-1] == '(':
        #             stack[-1] = 1
        #         else:
        #             temSum = 0
        #             while True:
        #                 temNum = stack.pop()
        #                 # print(temNum)
        #                 if temNum == '(':
        #                     stack.append(temSum * 2)
        #                     break
        #                 else:
        #                     temSum += temNum
        # return sum(stack)
        ans = 0
        stack = [0]
        temp = 0
        opening = '('
        closing = ')'
        for char in S:
            if char == opening:
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)
            print(stack)
        return stack.pop()

    def scoreOfParentheses2(self, s: str) -> int:
        stk = []

        for c in s:
            if c == '(':
                stk.append(-1)
                cur = 0
            else:
                if stk[-1] == -1:
                    stk[-1] = 1
                else:
                    cur = 0
                    while stk[-1] > 0:
                        cur += stk.pop()
                    stk[-1] = cur << 1

        return sum(stk)


if __name__ == '__main__':
    s = Solution()
    S = '(()((())))'
    print(s.scoreOfParentheses(S))
