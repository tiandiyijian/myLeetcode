class Solution:

    def trailingZeroes(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # 其实只算5的个数就行了
        # 因为10是可以拆成2和5的，所以不需要考虑10
        # 而5的个数肯定不会大于2的个数
        # two = five = ten = 0
        # for i in range(1, n+1):
        #     while i % 10 == 0:
        #         ten += 1
        #         i //= 10
        #     while i % 5 == 0:
        #         five += 1
        #         i //= 5
        #     while i % 2 == 0:
        #         two += 1
        #         i >>= 1
        # return ten + min(two, five)
        
        ans = 0
        while n > 0:
            n //= 5
            ans += n
        return ans