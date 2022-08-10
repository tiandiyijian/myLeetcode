class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(exp):
            sign = 1
            tmp = 0
            x_cnt = 0
            num = 0

            for i, c in enumerate(exp):
                match c:
                    case '-' | '+':
                        num += sign * tmp
                        tmp = 0
                        sign = -1 if c == '-' else 1
                    case 'x':
                        if i == 0 or (i > 0 and exp[i-1] in ('-', '+')):
                            x_cnt += sign
                        else:
                            x_cnt += sign * tmp
                            tmp = 0
                    case _:
                        tmp = tmp * 10 + ord(c) - ord('0')
            
            num += sign * tmp
            return x_cnt, num            


        left, right = equation.split('=')
        
        x_cnt, num = parse(left)
        # print(left, x_cnt, num)
        x_cnt_right, num_rgiht = parse(right)
        # print(right, x_cnt_right, num_rgiht)
        
        x_cnt -= x_cnt_right
        num -= num_rgiht

        if x_cnt == 0:
            return 'Infinite solutions' if num == 0 else 'No solution'
        
        return f'x={-num//x_cnt}'


e = "x+5-3+x=6+x-2"
e = "x=x"
e = "2x=x"
e = "0x=0"
print(Solution().solveEquation(e))

