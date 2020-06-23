from itertools import zip_longest


'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        i = 0
        llength = 0
        num = 0
        if la > lb:
            llength = lb
            num = la - lb
            b = '0' * num + b
            i = la - 1
        elif la < lb:
            llength = la
            num = lb - la
            a = '0' * num + a
            i = lb - 1
            tem = a
            a = b
            b = tem
        else:
            i = la - 1
        a = list(a)
        b = list(b)
        jinwei = 0
        while i >= 0:
            sum = str(int(a[i]) ^ int(b[i]) ^ jinwei)
            jinwei = (int(a[i]) & int(b[i])) | (int(a[i]) & jinwei) | (int(b[i]) & jinwei)
            a[i] = str(sum)
            print(a[i], jinwei)
            i -= 1
            if i < num and jinwei == 0:
                break
        if jinwei == 1:
            return '1' + ''.join(a)
        return ''.join(a)
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lena, lenb = len(a), len(b)
        if lena < lenb:
            a, b = b, a
            lena, lenb = lenb, lena
        ans = ""
        carry = 0
        # print(a, b)
        for i in range(-1, -1-lenb, -1):
            n1, n2 = int(a[i]), int(b[i])
            tmp_sum = (n1 + n2 + carry) % 2
            carry = (n1 + n2 + carry) // 2
            ans = str(tmp_sum) + ans
            # print(carry, tmp_sum)
            # print(f'i={i}')
        i -= 1
        while i >= -lena:
            # print(f'i={i}')
            n1 = int(a[i])
            tmp_sum = (n1 + carry) % 2
            carry = (n1 + carry) // 2
            ans = str(tmp_sum) + ans
            i -= 1
            # print(carry, tmp_sum)
        if carry == 1:
            return '1' + ans
        return ans

    def add2(self, a, b):
        ans = ''
        carry = 0
        for n1, n2 in zip_longest(a[::-1], b[::-1], fillvalue=0):
            n1, n2 = int(n1), int(n2)
            tmp_sum = (n1 + n2 + carry) % 2
            carry = (n1 + n2 + carry) // 2
            ans = str(tmp_sum) + ans
        if carry == 1:
            return '1' + ans
        return ans            


if __name__ == "__main__":
    S = Solution()
    a = '1010'
    b = '1011'
    print(S.add2(a, b))