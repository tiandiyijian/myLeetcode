class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1, idx2 = len(num1) - 1, len(num2) - 1
        ans = ''
        carry = 0
        while idx1 >= 0 and idx2 >= 0:
            ans = str((ord(num1[idx1]) - 48 + ord(num2[idx2]) - 48 + carry) % 10) + ans
            carry = (ord(num1[idx1]) - 48 + ord(num2[idx2]) - 48 + carry) // 10
            idx1 -= 1
            idx2 -= 1
        while idx1 >= 0:
            if carry == 0:
                return num1[:idx1+1] + ans
            ans = str((ord(num1[idx1]) - 48 + carry) % 10) + ans
            carry = (ord(num1[idx1]) - 48 + carry) // 10
            idx1 -= 1
        while idx2 >= 0:
            if carry == 0:
                return num2[:idx2+1] + ans
            ans = str((ord(num2[idx2]) - 48 + carry) % 10) + ans
            carry = (ord(num2[idx2]) - 48 + carry) // 10
            idx2 -= 1
        if carry == 1:
            return '1' + ans
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings('4', '69'))
