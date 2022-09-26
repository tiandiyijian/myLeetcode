from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums)

        xor_sum = 0
        for i in range(1, n + 3):
            xor_sum ^= i
        for num in nums:
            xor_sum ^= num

        lsb = xor_sum & (-xor_sum)  # 最低位的1
        # 根据lsb可以把所有数字分成两类
        # 一类是第l位为0一类为1

        a = xor_sum
        for i in range(1, n + 3):
            if i & lsb:
                a ^= i
        for num in nums:
            if num & lsb:
                a ^= num

        return [a, a ^ xor_sum]
