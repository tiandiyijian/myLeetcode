class Solution:

    def hasAlternatingBits(self, n: int) -> bool:
        # pre = n & 1
        # n >>= 1
        # while n > 0:
        #     cur = n & 1
        #     # print(pre, cur)
        #     if cur == pre:
        #         return False
        #     pre = cur
        #     n >>= 1
        # return True

        a = n ^ (n >> 1)  # 当且仅当n的二进制表示0、1交替时a才会全为1
        return a & (a + 1) == 0  # 当且仅当a&(a+1)=0时a的二进制位表示才会全为1
