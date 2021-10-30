from functools import reduce
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 关键在于怎么把这两个只出现一次的数字区分开, 可以使用xor_sum的最低位来区分, 因为在那一位上那两个只出现一次的数字肯定一个是1一个是0
        xor_sum = reduce(lambda x, y : x ^ y, nums)
        low_bit = xor_sum & (-xor_sum)
        ans = []
        xor_sum0 = xor_sum1 = 0
        for num in nums:
            if num & low_bit == 0:
                xor_sum0 ^= num
            else:
                xor_sum1 ^= num
        return [xor_sum0, xor_sum1]

