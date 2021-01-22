from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        ans = []
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            tmp = K % 10
            K //= 10
            s = tmp + A[i] + carry
            ans.append(s % 10)
            carry = s // 10
        while K:
            tmp = K % 10
            K //= 10
            s = tmp + carry
            carry = s // 10
            ans.append(s % 10)
        if carry:
            ans.append(1)
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    print()
