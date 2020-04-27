import time

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or num1 == '0' or num2 == '0': return '0'
        len1, len2 = len(num1), len(num2)
        digits = [0] * (len1 + len2)
        for i in range(len1-1, -1, -1):
            for j in range(len2-1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + digits[i + j + 1]
                digits[i + j + 1] = tmp % 10
                digits[i + j] += tmp // 10
        ans = ''
        # print(digits)
        for digit in digits:
            if digit != 0 or ans:
                ans += str(digit)
        # print(ans)
        return ans

# class Solution:
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         num1_len, num2_len = len(num1), len(num2)
#         res = ['0'] * (num1_len + num2_len)
#         for j in range(num1_len-1, -1, -1):
#             for i in range(num2_len-1, -1, -1):
#                 tmp = int(num1[j]) * int(num2[i]) + int(res[i + j + 1])
#                 res[i + j + 1] = str(tmp%10)
#                 res[i + j] = str(int(res[i+j]) + tmp // 10)
                
#         for i in range(num1_len + num2_len):
#             if res[i] != '0':
#                 return ''.join(res[i:])
#         return '0'



if __name__ == "__main__":
    s = Solution()
    t = time.time()
    print(s.multiply('314', '48'))
    print(time.time() - t)
        
